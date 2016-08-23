#!/usr/bin/python

import sys, os, argparse, math, time


#
# Authors : Henri Crombe and Mallory Declercq (for the completion of a Master Thesis in Computer Science at Polytechnic School of Louvain)
#
# This script has been written to perform and assess the performance of correlation attacks against Tor circuits.
#
# It receives as input :
# 1) The correlation technique to apply : basic_approach | packet_counting | cross_correl
# 2) The name of clients to target : web | irc  | ssh | bulk 
# 3) The path to the Shadow log file of the experiment to analyze (ex: shadow.log )
# 4) The path to the directory storing the results of the shadow experiment (ex: shadow.data/hosts/ ) 
# 5) The path to the directory storing the results of the attack
#
# The script retrieves from the Tor controller logs all the circuits that that passes at Tor relays (Tor logs must be generated with the modified version of Tor)
# The script then correlates all the entry  circuits (firt_hop) against all the exit circuits (last_hop) that exists during the interval of correlation.
# The script eventually finishes by computing and storing the FPR and FNR as well as the TP, TN, FP and FN counts for different thresholds.
#
#


# Main function starts here
def main():
	# Get args
	correlation_technique = sys.argv[1]  # Correlation technique to use : basic_approach | packet_counting | cross_correl
	client_type = sys.argv[2] # Client type to target : web | irc  | ssh | bulk
	shadow_log_path = sys.argv[3] # Path to the log file of the Shadow experiment
	log_directory = sys.argv[4] # Path to the result directory of the Shadow experiment (ex: shadow.data/hosts/ ) 
	result_dir = sys.argv[5] # directory path for the results
	
	# Start timer
	start_exec = time.time()
	
	# Parse shadow log and return a list of TorNode with name and IP address for each node
	print('Parse shadow log')
	torNodes = parse_shadow_log_get_nodes(shadow_log_path)
	target_IP_dict = get_target_IP(torNodes)

	print('Parse tor controller logs')
	parse_relay_tor_controller_logs(log_directory, torNodes, target_IP_dict) #parse relays logs
	parse_client_tor_controller_logs(log_directory,torNodes) # pase clients logs

	#Mark interesting entry circuits to correlated
	print('Marking interesting entry circuits to correlate')
	mark_used_entry_circuits(torNodes,target_IP_dict)


	#Now every Tor node are initialized with their circuits
	#The nodes only remember the circuit that originiate 
	#from a victim if the node is the first or last hop of the circuit
	print('Correlate circuits')
	results = correlate_circuits(torNodes, target_IP_dict, client_type, correlation_technique)
	print('Parsing and Correlation finished in '+str(time.time()-start_exec)+' seconds')

	# Save results for each threshold for a given type of client
	save_results(result_dir, results, client_type, correlation_technique)


# Define classes 
# Circuit class represents a circuit at a Tor relay.
# It stores the cell traffic pattern and other information recorded by the Tor controller
class Circuit:
	def __init__(self):
		self.is_first_hop = False
		self.is_last_hop  = False
		self.has_been_used = False
		self.is_to_correlate = False

		self.IP_origin = ''
		self.circID_at_origin = -1
		self.created_at = -1 # time t (in s) when the circuit was created (receive create_cell)
		self.used_at = -1
		self.cells_written = {} # Nbr of cells written at time t in backward direction

	def print_circ(self):
		print('Circ stat -> Origin : '+self.IP_origin+' ID at origin : '+str(self.circID_at_origin)+' is_first_hop='+str(self.is_first_hop) +' created at :'+str(self.created_at)+' used_at: '+str(self.used_at))

# TorNode class can either represent a relay or a client.	
# It stores the name, the IP address and the list of circuits that belongs to the relay/client.
class TorNode:
	def __init__(self, name):
		self.name = name

	def __init__(self, name, ip):
		self.is_client = False
		self.name = name
		self.IP_address = ip
		self.circuit_list = []

	def print_node(self):
		print('Node : '+self.name+' IP : '+self.IP_address+' is_client='+str(self.is_client))



###
# Correlate_circuits function is in charge of correlating all the entry circuits that belongs
# to 'client_type' against all exit circuits that exist during the correlation interval. 
# The function computes the FNR, FPR and the FP,FN,TP,TN counts at the end of the attack.
###
def correlate_circuits(torNodes, target_IP_dict, client_type, correlation_technique):

	# Initialize vars and tabs to store results
	TP_count = []
	TN_count = []
	FP_count = []
	FN_count = []

	TP = [[] for i in range(10)]
	TN = [[] for i in range(10)]
	FP = [[] for i in range(10)] 
	FN = [[] for i in range(10)]

	for i in range(0, 10):
		TP_count.append(0)
		TN_count.append(0)
		FP_count.append(0)
		FN_count.append(0)

	distance_results = [] #for packet-counting technique
	distance_max = 0 #for packet-counting technique

	results = []

	nbr_entry_flow_correlated = 0
	mean_concurent_circ = 0
	c = 0

	# Start correlating circuits
	# For every entry circuit that is worth correlating (i.e. First_hop & Belong to targeted client & Dirty),
	# correlate against all exit circuits that carry at least one cell (downward) during the interval of correlation.
	for n in torNodes:
		if 'relay' in torNodes[n].name or 'exit' in torNodes[n].name:
			print('Start correlating circuits transiting on Tor node :  '+torNodes[n].name)
			for circuit in torNodes[n].circuit_list:
				if circuit.is_first_hop == True and circuit.has_been_used == True and circuit.IP_origin in target_IP_dict.keys() and circuit.is_to_correlate==True:
					# The entry circuit is marked as First_hop & dirty 
					if client_type not in target_IP_dict[circuit.IP_origin]:
						# Not the type of client to correlate, next !
						continue

					# if cell_count(circuit.cells_written) > 0:
					# 	#print('Circuit at entry not interesting')
					# 	continue

					nbr_entry_flow_correlated += 1
					entry_flow = circuit.cells_written # get entry circuits cell flow pattern (cell/s)

					start_time = circuit.used_at # start to correlate when the circuit has been marked as dirty by the client
					stop_time = start_time + 600 # end correlation interval after 10 minutes

					mu_1 = compute_mean(entry_flow,int(start_time),int(stop_time),1) # pre-compute the average number of cell sent per second

					# Correlate the entry circuit against all exit circuits
					nbr_exit_circ_to_correlate = 0
					for last_hop in torNodes:
						if 'relay' in torNodes[last_hop].name or 'exit' in torNodes[last_hop].name:
							if torNodes[last_hop].name == torNodes[n].name:
								# Don't correlate circuits from the current node
								continue

							# For every circuit that is marked as Last_hop needs to be correlated 
							for exit_circuit in torNodes[last_hop].circuit_list:
								if exit_circuit.is_last_hop == True:

									exit_flow = exit_circuit.cells_written # get cell traffic pattern of the exit circuit (downward flow)
									
									exit_flow_cell_count = cell_count_interval(exit_flow, start_time, stop_time)

									if exit_flow_cell_count == 0:
										# No cell going downward at exit circuit during interval of correlation -> not interesting
										continue

									nbr_exit_circ_to_correlate += 1
									
									# Correlate entry vs current exit circuit
									correlation_value = correlate(correlation_technique, entry_flow, exit_flow, start_time, stop_time, mu_1, 0, 1)
									
									# Save max distance value for packet counting strategy
									if correlation_technique == 'packet_counting' and correlation_value > distance_max:
										distance_max = correlation_value
									

									client_name = target_IP_dict[circuit.IP_origin]
									result_description = {'client_name':client_name,'circ_ID':circuit.circID_at_origin,'correlation':correlation_value,'entry':n,'exit':last_hop}

									if correlation_technique == 'packet_counting':
										if(circuit.IP_origin == exit_circuit.IP_origin and circuit.circID_at_origin == exit_circuit.circID_at_origin):
											result_description['is_match'] = True
										else:
											result_description['is_match'] = False

										distance_results.append(result_description)

									else:
										# For basic_approach and cross_correl
										# Compute TP, TN, FP and FN for threshold varying from 0 and 1.
										# This step is quite overkill but we first construct the script this way
										# Results will be stored on disk later and are be used for further analysis
										for thresh in range(0, 10):
											t = float(thresh)/10.0
												
											if(circuit.IP_origin == exit_circuit.IP_origin and circuit.circID_at_origin == exit_circuit.circID_at_origin):

												#We found the corresponding exit circuit
												if correlation_value >= t :
													#it's a true-positive
													TP_count[thresh] += 1
													TP[thresh].append(result_description)

												else:
													#it's a false-negative result
													FN_count[thresh] += 1
													FN[thresh].append(result_description)
			
											else:
												# It's not a match (entry and exit are not related)
												if correlation_value < t :
													#True negative
													TN_count[thresh] += 1
													TN[thresh].append(result_description)
												else:
													# correlation_value > thresh -> false positive
													FP_count[thresh] += 1
													FP[thresh].append(result_description)

								
					mean_concurent_circ += nbr_exit_circ_to_correlate	
					c += 1


	# Normalize results for packet_counting techique with distance max observed
	if correlation_technique == 'packet_counting':
		print('Normalize distances')
		print('Distance max observed  '+str(distance_max))
		for r in distance_results:
			correl_value = 0
			if distance_max == 0 :
				# Should never happen ...
				print('Distance max == 0 !')
				print('Distance not Normalized : '+str(r['correlation']))


			else:
				# correlation value = 1 - d(x,y)/d_max
				correl_value = 1 - ( float(r['correlation']) / distance_max )

			for thresh in range(0, 10):
				t = float(thresh)/10.0

				r['correlation'] = correl_value

				if r['is_match'] == True:
					if correl_value >= t:
						TP_count[thresh] += 1
						TP[thresh].append(r)
					else:
						FN_count[thresh] += 1
						FN[thresh].append(r)
				else:
					if correl_value < t:
						TN_count[thresh] += 1
						TN[thresh].append(r)
					else:
						FP_count[thresh] += 1
						FP[thresh].append(r)


	mean_concurent_circ_at_exit = 0
	if c > 0:
		mean_concurent_circ_at_exit = float(mean_concurent_circ) / float(c)
	else:
		mean_concurent_circ_at_exit = -1

	print('Mean concurrent circuits at exit relays : '+str(mean_concurent_circ_at_exit))

	results = [ [TP,TP_count], [TN,TN_count], [FP,FP_count], [FN,FN_count], [mean_concurent_circ_at_exit,nbr_entry_flow_correlated] ]
	return results



###
# Correlate function is used to actually compute the correlation value between two cell flows.
# Three different correlation techniques are implemented : basic_approach, packet_counting, cross-correlation
# The cross-correlation function can be used with a specified 'network_delay' and 'window_size'
###
def correlate(technique, traffic_entry, traffic_exit, start_time, stop_time, mu_1, network_delay, window_size):
	if technique == 'cross_correl':
		mu_2 = compute_mean(traffic_exit,start_time,stop_time,1)
		d = network_delay
		res_num = 0.0
		res_den = 0.0
		deno_part1 = 0.0
		deno_part2 = 0.0
		res= 0.0

		for t in range(start_time, stop_time+1, window_size):
			x_i = 0.0
			x_id_prime = 0.0

			for i in range(0, window_size):
				if str(t+i) in traffic_entry:
					x_i += traffic_entry[str(t+i)]
				if str(t+i-d) in traffic_exit:
					x_id_prime += traffic_exit[str(t+i-d)]

			res_num    = res_num + ((x_i - mu_1) * (x_id_prime - mu_2))
			deno_part1 = deno_part1 + ((x_i - mu_1) * (x_i - mu_1))
			deno_part2 = deno_part2 + ((x_id_prime - mu_2) * (x_id_prime - mu_2))

		res_den = math.sqrt(deno_part1) * math.sqrt(deno_part2)

		if res_den == 0.0 :
			res = -1
		else :
			res = res_num / res_den

		return res

	elif technique == 'basic_approach':
		entry_activity_flow = get_activity_flow(traffic_entry,start_time,stop_time)
		exit_activity_flow  = get_activity_flow(traffic_exit,start_time,stop_time)

		res_num = 0.0
		res_deno = 0.0
		correlation_result = 0.0

		for t in range(start_time, stop_time+1):
			res_num += entry_activity_flow[t] * exit_activity_flow[t]

		for t in range(start_time, stop_time+1):
			res_deno += entry_activity_flow[t]

		if res_deno != 0.0:
			correlation_result = res_num / res_deno
		
		return correlation_result

	elif technique == 'packet_counting':
		entry_cell_count = cell_count_interval(traffic_entry,start_time,stop_time)
		exit_cell_count = cell_count_interval(traffic_exit,start_time,stop_time)

		distance = math.sqrt((entry_cell_count - exit_cell_count)**2)

		return distance

	else:
		print('Correlation technique not recognized !')
		return -1


###
# This function marks the entry circuits as to correlate if the clients have effectively used them to carry data.
###
def mark_used_entry_circuits(torNodes, target_IP_dict):
	interesting_circuit_count = 0

	for n in torNodes:
		if 'relay' in torNodes[n].name or 'exit' in torNodes[n].name:
			for circuit in torNodes[n].circuit_list:
				is_circ_interesting = False

				if circuit.is_first_hop == True and circuit.has_been_used == True and circuit.IP_origin in target_IP_dict.keys():

					for last_hop in torNodes:
						if 'relay' in torNodes[last_hop].name or 'exit' in torNodes[last_hop].name:

							for exit_circuit in torNodes[last_hop].circuit_list:
								if exit_circuit.is_last_hop == True:
									exit_flow = exit_circuit.cells_written
									exit_flow_cell_count = cell_count(exit_flow)
									if exit_flow_cell_count == 0:
										#no traffic going downward at exit circuit -> not interesting
										continue

									if(circuit.IP_origin == exit_circuit.IP_origin and circuit.circID_at_origin == exit_circuit.circID_at_origin):
										is_circ_interesting = True

				circuit.is_to_correlate = is_circ_interesting
				if is_circ_interesting == True:
					interesting_circuit_count += 1

	print('Interesting circuit count : '+str(interesting_circuit_count))


###
# Compute the average number of cell that are transferer per second on 'cell_flow' durint the interval [start_time;stop_time]
###
def compute_mean(cell_flow,start_time,stop_time, window_size):
	if start_time == stop_time:
		return float(cell_flow[str(start_time)])

	mean = 0.0
	total = 0.0
	number_of_windows = 0

	for t in range(start_time, stop_time+1, window_size):
		for i in range(0, window_size):
			if str((t+i)) in cell_flow.keys():
				
				total += cell_flow[str(t+i)]

		number_of_windows += 1

	mean = total / number_of_windows

	return mean


def get_activity_flow(cell_flow, start_time, stop_time):
	activity_flow = {}

	for t in range(start_time, stop_time+1):
		if str(t) in cell_flow.keys() and cell_flow[str(t)] > 0:
			activity_flow[t] = 1
		else:
			#no activity in time t
			activity_flow[t] = 0

	return activity_flow


def cell_count_interval(cell_flow, start_time, stop_time):
	cell_count = 0

	for t in range(start_time, stop_time+1):
		if str(t) in cell_flow.keys() and cell_flow[str(t)] > 0:
			cell_count += cell_flow[str(t)]

	return cell_count


def cell_count(cell_flow):
	count = 0
	for k in cell_flow.keys():
		count += cell_flow[k]
	return count 


def count_nbr_relay_cell(line_part):
	
	cells = line_part.split('=')[1]
	count = 0

	for c in cells.split(','):
		if 'relay' in c:
			count = int(c.split(':')[1])

	return count


def get_connection_timings(cell_flow):
	start = 0
	stop =  0
	first = True

	for t in sorted(cell_flow.keys()):
		if first == True:
			start = t
			first = False

		stop = t

	return [start,stop]


def parse_relay_tor_controller_logs(log_directory, torNodes, target_IP_dict):
	for t in torNodes:
		if 'relay' in torNodes[t].name.lower() or 'exit' in torNodes[t].name.lower() or 'thori' in torNodes[t].name.lower() :
			#print(torNode.name)
			log_path = log_directory+torNodes[t].name+'/stdout-torctl-1001.log'
			if os.path.isfile(log_path):
				parse_torctl_file(log_path, torNodes[t].name, torNodes, target_IP_dict)


def parse_torctl_file(path, node_name, torNodes, target_IP_dict):
	log_file = open(path,'r')
	circuits = {}

	for line in log_file:
		if 'CELL_STATS' in line:
			params = line.strip().split()

			if(len(params) < 10):
				continue

			if 'CIRCUIT_RELAY_FIRST_HOP' == params[9] or 'CIRCUIT_RELAY_LAST_HOP' == params[9]:

				cur_circ_origin_IP = params[11].split('=')[1]
				cur_circ_ID = params[10].split('=')[1]
				
				k = cur_circ_origin_IP +'*'+ cur_circ_ID
				k = k.strip()

				if k not in circuits:
					# First appearance of originIP+circID_at_origin in log, create new Circuit
					circ = Circuit()
					if 'CIRCUIT_RELAY_FIRST_HOP'  == params[9]:
						circ.is_first_hop=True
					else:
						circ.is_last_hop=True

					# Initialize circuit information
					circ.IP_origin = cur_circ_origin_IP
					circ.circID_at_origin = int(cur_circ_ID)
					circ.created_at = int(params[12].split('=')[1])
					circuits[k] = circ

				tick = params[2].split('.')[0]
				if tick not in circuits[k].cells_written:
					# Add the number of cell that was transmitted in the backward direction at tick (second)
					# Cell_written forms the cell traffic pattern to analyze
					circuits[k].cells_written[tick] = 0

				if 'Outbound' in params[15]:
					#no traffic is going appward -> 0 cell transited at tick t 
					continue

				cell_count = count_nbr_relay_cell(params[15])
				circuits[k].cells_written[tick] = cell_count

			else: 
				continue 

	for c in circuits:
		# Add all parsed circuits to the circuit_list of the current torNode
		torNodes[node_name].circuit_list.append(circuits[c])

	log_file.close()


def get_target_IP(torNodes):
	ip_dict = {} # key=victimIP value=name

	for node in torNodes:
		if 'client' in torNodes[node].name.lower():
			ip_dict[torNodes[node].IP_address] = torNodes[node].name.lower()
			
	return ip_dict


def parse_shadow_log_get_nodes(shadow_log_path):
	log_file = open(shadow_log_path,'r')
	torNodes = {}

	for line in log_file:
		if 'host_new' in line:
			#parse the line 
			params = line.strip().split()
			node_name = params[9].split(',')[0]
			node_name = node_name[1:-1]
			ip = params[11]
			ip = ip[:-1]

			cur_node = TorNode(node_name.lower(), ip)
			t = node_name.lower()
			if 'client' in t or 'webclient' in t or 'bulkclient' in t or 'ircclient' in t or 'sshclient' in t:
				cur_node.is_client = True
			
			torNodes[cur_node.name.lower()] = cur_node

	log_file.close()

	return torNodes


def parse_client_tor_controller_logs(log_directory,torNodes):
	for t in torNodes:
		if 'client' in torNodes[t].name.lower():
			#print(torNode.name)
			log_path = log_directory+torNodes[t].name+'/stdout-torctl-1001.log'
			if os.path.isfile(log_path):
				parse_client_torctl_file(log_path, torNodes[t].name, torNodes)


def parse_client_torctl_file(log_path, node_name, torNodes):
	log_file = open(log_path,'r')
	used_circuits = {} #keys = IP*ID value=dirty_timestamp

	for line in log_file:
		if 'CELL_STATS' in line:
			params = line.strip().split()

			if(len(params) < 10):
				continue	

			if params[9] == 'CIRCUIT_ORIGINATING_HERE':
				if 'CIRCUIT_HAS_BEEN_USED' in params[11]:
					timestamp_dirty = params[11].split('=')[1]
					local_id = params[10].split('=')[1]
					node_ip = torNodes[node_name].IP_address
					key = node_ip+'*'+local_id
					used_circuits[key] = int(timestamp_dirty)
					
	for n in torNodes:
		if 'relay' in torNodes[n].name or 'exit' in torNodes[n].name or 'thori' in torNodes[n].name  :
			#print(torNodes[n].name)
			for circuit in torNodes[n].circuit_list:
				#circuit.print_circ()
				key = circuit.IP_origin+'*'+str(circuit.circID_at_origin)
				#print(key)
				if key in used_circuits.keys():
					
					circuit.has_been_used = True
					circuit.used_at = used_circuits[key]

###
# This function saves the results obtained at the end of the attack.
# It creates the files that stores the FP, FN, TP and TN results for the attack for different thresholds [0,0.1,...,1]
# A summary of the attack is given for the different threshold.
# Note that it is overkill to store the data for different threshold as the results and analyzed using the results for one threshold
###
def save_results(result_dir, results, client_type, correlation_technique):
	print('Saving results in '+result_dir)
	if not os.path.exists(result_dir):
		os.makedirs(result_dir)

	for t in range(0,10):
		thresh= float(t)/10.0

		r_path = result_dir+'client_'+client_type+'_technique_'+correlation_technique+'_thresh_'+str(thresh)

		if not os.path.exists(r_path):
			os.makedirs(r_path)

		TN_file = open(r_path+'/TN_'+client_type+'_thresh_'+str(thresh)+'.csv', 'w+')
		TP_file = open(r_path+'/TP_'+client_type+'_thresh_'+str(thresh)+'.csv', 'w+')
		FP_file = open(r_path+'/FP_'+client_type+'_thresh_'+str(thresh)+'.csv', 'w+')
		FN_file = open(r_path+'/FN_'+client_type+'_thresh_'+str(thresh)+'.csv', 'w+')

		save_to_csv(TP_file, results[0][0][t])
		save_to_csv(TN_file, results[1][0][t])
		save_to_csv(FP_file, results[2][0][t])
		save_to_csv(FN_file, results[3][0][t])

		#make summary for this threshold
		summary_file = open(r_path+'/summary_'+client_type+'_thresh_'+str(thresh)+'.txt', 'w+')

		TP_count =  results[0][1][t]
		TN_count =  results[1][1][t]
		FP_count =  results[2][1][t]
		FN_count =  results[3][1][t]

		FPR = -1
		FNR = -1

		if FP_count + TN_count > 0 and FN_count + TP_count > 0:
			FPR = float(FP_count) / float(FP_count + TN_count)
			FNR = float(FN_count) / float(FN_count + TP_count)

		summary_file.write('Client type : '+str(client_type)+'\n')
		summary_file.write('Correlation technique : '+correlation_technique)
		summary_file.write('Threshold   : '+str(thresh)+'\n')
		summary_file.write('Number of entry flow correlated : '+str(results[4][1])+'\n')
		summary_file.write('Number of concurrent exit flows (mean value) : '+str(results[4][0])+'\n')
		summary_file.write('FPR   : '+str(FPR)+'\n')
		summary_file.write('FNR   : '+str(FNR)+'\n')
		summary_file.write('TP    : '+str(TP_count)+'\n')
		summary_file.write('TN    : '+str(TN_count)+'\n')
		summary_file.write('FP    : '+str(FP_count)+'\n')
		summary_file.write('FN    : '+str(FN_count)+'\n')

		TN_file.close()
		TP_file.close()
		FP_file.close()
		FN_file.close()
		summary_file.close()


def save_to_csv(file, result_tab):
	file.write('name,value\n')

	for r in result_tab:
		#{'client_name':client_name,'circ_ID':circuit.circID_at_origin,'correlation':rd,'entry':n,'exit':last_hop}
		file.write(''+str(r['client_name'])+','+str(r['correlation'])+'\n')



if __name__ == '__main__': sys.exit(main())
