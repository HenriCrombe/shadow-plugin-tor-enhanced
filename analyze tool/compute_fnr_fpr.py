#!/usr/bin/python

import matplotlib; matplotlib.use('Agg') # for systems without X11
from matplotlib.backends.backend_pdf import PdfPages
import sys, os, argparse, subprocess, json, pylab, numpy


def main():

	###
	# The script receives as input :
	# 1) Path of the directory storing TP, FN, FP, TN  csv files (output of analyze_circuits.py)
	# 2) A threshold value : between 0 and 1 (or -1 and 1 for cross-correlation)
	#
	# The script computes and print the FNR, FPR and the P( I=J | I~J) given the TP, FN, FP, TN  csv files given as input
	###

	threshold = sys.argv[2]

	for f in os.listdir(sys.argv[1]):
		# Open csv files containing the results of the analyze_circuits.py script	
		if 'TP' in f:
			TP_file = open(sys.argv[1]+f,'r')
		elif 'TN' in f:

			TN_file = open(sys.argv[1]+f, 'r')
		elif 'FP' in f:
			FP_file = open(sys.argv[1]+f, 'r')
		elif 'FN' in f:
			FN_file = open(sys.argv[1]+f, 'r')

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

	# Compute the FPR and FNR for the given threhsold 
	results = compute_fpr_fnr(x1_tab,x2_tab, threshold)

	# OR compute the max probability P( I=J | I~J) achievable
	#results = compute_max_prob(x1_tab,x2_tab)

	FPR = results[0]
	FNR = results[1]

	pij = 0.001 # 1000 concurrent exit flows -> P(I=J) = 1 / 1000
	deno = (((1 - FNR - FPR) * pij) + FPR)

	proba = 0.0
	if deno == 0 or FNR > 0.5 or FPR > 0.5 : 
		proba = 0.0
	else :
		proba = ((1-FNR) * pij) / deno


	print "FNR : %.6f" % FNR + " & FPR : %.6f " % FPR + " &  P(I=J | I~J) : %.6f" % proba



def compute_fpr_fnr(match_tab, non_match_tab, thresh):
	match_tab = sorted(match_tab)  # TP and FN -> results for matching circuits
	non_match_tab = sorted(non_match_tab) # TN and FP -> results for non-matching circuits

	FN_count = count_threshold(match_tab, thresh)
	TP_count = len(match_tab) - FN_count

	TN_count = count_threshold(non_match_tab, thresh)
	FP_count = len(non_match_tab) - TN_count

	FPR = 0.0
	FNR = 0.0

	if FP_count + TN_count > 0 and FN_count + TP_count > 0:
		FPR = float(FP_count) / float(FP_count + TN_count)
		FNR = float(FN_count) / float(FN_count + TP_count)


	return [FPR,FNR]


def compute_max_prob(match_tab,non_match_tab):
	match_tab = sorted(match_tab)  # TP and FN -> results for matching circuits
	non_match_tab = sorted(non_match_tab) # TN and FP -> results for non-matching circuits
	max_prob = 0.0
	max_thresh = 0.0
	max_fpr = 0.0
	max_fnr = 0.0

	results = []
	i = 0

	for t in range(i,100001):
		thresh= float(t)/100000.0

		FN_count = count_threshold(match_tab, thresh)
		TP_count = len(match_tab) - FN_count

		TN_count = count_threshold(non_match_tab, thresh)
		FP_count = len(non_match_tab) - TN_count

		FPR = 0.0
		FNR = 0.0

		if FP_count + TN_count > 0 and FN_count + TP_count > 0:
			FPR = float(FP_count) / float(FP_count + TN_count)
			FNR = float(FN_count) / float(FN_count + TP_count)

		pij = 0.001
		deno = (((1 - FNR - FPR) * pij) + FPR)

		if deno == 0 or FNR > 0.5: 
			proba = 0.0
		else :
			proba = ((1-FNR) * pij) / deno

		if proba > max_prob:
			max_prob = proba
			max_thresh = thresh
			max_fpr = FPR
			max_fnr = FNR

	return [max_prob,max_thresh,max_fpr,max_fnr]


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
