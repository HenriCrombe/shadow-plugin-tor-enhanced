#!/usr/bin/python

import matplotlib; matplotlib.use('Agg') # for systems without X11
from matplotlib.backends.backend_pdf import PdfPages
import sys, os, argparse, subprocess, json, pylab, numpy
from itertools import cycle

pylab.rcParams.update({
	'backend': 'AGG',
	'font.size': 16,
	'figure.figsize': (6,4.5),
	'figure.dpi': 100.0,
	'figure.subplot.left': 0.15,
	'figure.subplot.right': 0.95,
	'figure.subplot.bottom': 0.15,
	'figure.subplot.top': 0.95,
	'grid.color': '0.1',
	'axes.grid' : True,
	'axes.titlesize' : 'small',
	'axes.labelsize' : 'small',
	'axes.formatter.limits': (-4,4),
	'xtick.labelsize' : 'small',
	'ytick.labelsize' : 'small',
	'lines.linewidth' : 2.0,
	'lines.markeredgewidth' : 0.5,
	'lines.markersize' : 10,
	'legend.fontsize' : 'x-small',
	'legend.fancybox' : False,
	'legend.shadow' : False,
	'legend.borderaxespad' : 0.5,
	'legend.numpoints' : 1,
	'legend.handletextpad' : 0.5,
	'legend.handlelength' : 1.6,
	'legend.labelspacing' : .75,
	'legend.markerscale' : 1.0,
	# turn on the following to embedd fonts; requires latex
	#'ps.useafm' : True,
	#'pdf.use14corefonts' : True,
	#'text.usetex' : True,
})
	
try: pylab.rcParams.update({'figure.max_num_figures':50})
except: pylab.rcParams.update({'figure.max_open_warning':50})
try: pylab.rcParams.update({'legend.ncol':1.0})
except: pass
	
def main():

	###
	# The script receive as input :
	# 1) Path to a text file containting a list graphs to make -> ex file line : packet_count_web, path_of_directory_storing_TP_TN_FP_FN_csv_files
	# 2) Path of the directory that will store the results 
	#
	# The scripts is in charge of making the graphs showing the FNR and FPR curves as well as the EER obtained.
	###

	list_file = open(sys.argv[1],'r') # Path to the file containing the list of graphs to make
	result_file_path = sys.argv[2] 

	for line in list_file:
		#print(line)
		# typical line : name_of_graph_to_make, path_of_directory_storing_TP_TN_FP_FN_csv_files
		parts = line.strip().split(',')

		result_graph_name = result_file_path+parts[0]

		for f in os.listdir(parts[1]):
			# Open csv files containing the results of the analyze_circuits.py script
			if 'TP' in f:
				TP_file = open(parts[1]+f,'r')
			elif 'TN' in f:
				TN_file = open(parts[1]+f, 'r')
			elif 'FP' in f:
				FP_file = open(parts[1]+f, 'r')
			elif 'FN' in f:
				FN_file = open(parts[1]+f, 'r')

		TP = extract_value_from_csv(TP_file)
		TN = extract_value_from_csv(TN_file)
		FP = extract_value_from_csv(FP_file)
		FN = extract_value_from_csv(FN_file)

		x1_tab = [] # TP and FN -> results for matching circuits
		x2_tab = [] # TN and FP -> results for non-matching circuits

		for v in TP:
			x1_tab.append(v)

		for v in FN:
			x1_tab.append(v)

		for v in TN:
			x2_tab.append(v)

		for v in FP:
			x2_tab.append(v)

		if 'correl' in parts[1]:
			technique = 'cross_correl'
		else:
			technique = 'other'

		# Compute the FNR and FPR for a threshold varying from 0 to 1 (or -1 to 1 for cross_correlation)
		results = compute_eer_tab(x1_tab, x2_tab, technique)
	 	
	 	EER = results[0][0]
	 	EER_thresh = results[0][1]
	 	results = results[1]

	 	x = []
		fpr = []
		fnr = []

		for r in results:
			x.append(r[0])
			fpr.append(r[1][0])
			fnr.append(r[1][1])
			
		pylab.figure("FNR_FPR")

		x1_line = pylab.plot(x, fpr, label="FPR", color='k')
		x2_line = pylab.plot(x, fnr, label="FNR",color='b', linestyle='-')

		text = 'EER : '+str(round(EER,6))+'\n Thresh : '+str(round(EER_thresh,5))

		pylab.plot(EER_thresh, EER, 'o', color='g')

		pylab.annotate(text, xy=(EER_thresh, EER), xycoords='data',
			xytext=(0.6, 0.5), textcoords='axes fraction',
			arrowprops=dict(facecolor='black', shrink=0.05),
			horizontalalignment='right', verticalalignment='top',
			)

		pylab.legend(loc='upper left')

		pylab.xlabel("Threshold")
		pylab.ylabel("FPR & FNR")

		if technique == 'other':
			pylab.xlim(xmin=-0.05,xmax=1.05)

		else:
			pylab.xlim(xmin=-0.1,xmax=1.05)

		pylab.yticks([0.2,0.4,0.6,0.8,1])
		pylab.savefig(result_graph_name, bbox_inches='tight')
		pylab.show()
		pylab.close()


def compute_eer_tab(match_tab, non_match_tab, correlation_technique):
	match_tab = sorted(match_tab)  # TP and FN -> results for matching circuits
	non_match_tab = sorted(non_match_tab) # TN and FP -> results for non-matching circuits

	results = []
	i = 0

	if correlation_technique == 'cross_correl':
		i = -100000

	delta = 1
	EER = 1
	EER_thresh = -1

	for t in range(i,100001):
		# Fix threshold and compute FNR and FPR. Then save results
		thresh= float(t)/100000.0

		FN_count = count_threshold(match_tab, thresh)
		TP_count = len(match_tab) - FN_count

		TN_count = count_threshold(non_match_tab, thresh)
		FP_count = len(non_match_tab) - TN_count

		FPR = 0
		FNR = 0

		if FP_count + TN_count > 0 and FN_count + TP_count > 0:
			FPR = float(FP_count) / float(FP_count + TN_count)
			FNR = float(FN_count) / float(FN_count + TP_count)


		if abs(FNR - FPR) < delta:
			# Find where difference between the FNR and FPR is the lowest possible to find the most precise EER.
			delta = abs(FNR - FPR)
			EER = FNR
			EER_thresh = thresh

		results.append([thresh,[FPR,FNR]])

	return [[EER, EER_thresh], results]

def count_threshold(tab, thresh):
	c = 0
	for v in tab:
		if v < thresh:
			c += 1
		else:
			return c

	return c 


def extract_value_from_csv(file):
	first = True
	values = []
	for line in file:
		if first == True:
			first = False
			continue
		

		if 'client' not in line:
			continue
			print('not a client')
		
		values.append(float(line.split(',')[1]))

	return values


if __name__ == '__main__': sys.exit(main())
