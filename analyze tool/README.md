## Analyzing tools
This directory holds the script used to perform correlation attacks against Tor circuits using the Tor controller logs generated using the modified Tor implementation. The directory also holds Python script that can be used and modified to analyze the output of the script 'analyze_circuits.py'.

# analyze_circuits.py

The script retrieves from the Tor controller logs all the circuits that that passes at Tor relays (Tor logs must be generated with the modified version of Tor) and correlates all the entry  circuits (firt_hop) against all the exit circuits (last_hop) that exists during the interval of correlation (that last 10 minutes). The script eventually finishes by computing and storing the FPR and FNR as well as the TP, TN, FP and FN counts for different thresholds (in csv files).

# make_fnr_fpr_eer_graphs.py

This script receive as input :
1) Path to a text file containting a list graphs to make 
   -> ex file line : packet_count_web , path_of_directory_storing_TP_TN_FP_FN_csv_files
2) Path of the directory that will store the results 

Then the script makes the graphs showing the FNR and FPR curves as well as the EER obtained.

# compute_fnr_fpr.py

The script receives as input :
1) Path of the directory storing TP, FN, FP, TN  csv files (output of analyze_circuits.py)
2) A threshold value : between 0 and 1 (or -1 and 1 for cross-correlation)

And computes and prints the FNR, FPR and the P( I=J | I~J) given the TP, FN, FP, TN  csv files given as input





