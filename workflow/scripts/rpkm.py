#!/usr/bin/env python3

#This script takes two inputs:
#1. a text file containing the number of reads
#2. a .bam.stat file created after running samtools idxstats on sorted bam files

import sys
import os
medlen_dict = {}

#opening pre-calculated median lengths for each of the genes in MEGARes database
with open('data/medians2211') as medfile:
	medf = medfile.read().split('\n')[:-1]
for line in medf:
	gene = line.split(' ')[0]
	count = float(line.split(' ')[1])
	medlen_dict[gene] = count

#first argument is a file containing the number of filtered reads
with open(sys.argv[1]) as readsfile:
	readsf = readsfile.read().split('\n')[:-1]
nreads = int(readsf[0])

#second argument is a .bam.stat file
#and we assume it is called "SRRXXXXXX.bam.stat"
#it's basename will be sample name
samplename = os.path.basename(sys.argv[2])[:-9]
cdict = {}
with open(sys.argv[2]) as statfile:
	statf = statfile.read().split('\n')[:-2]
	#there is a "*" in the last line of any .bam.stat file
for line in statf:
	#reading through MEGARes fasta header structure
	meg = line.split('\t')[0]
	gene = meg.split('|')[4]
	readcount = int(line.split('\t')[2])
	if not gene in cdict:
		cdict[gene] = readcount
	else:
		cdict[gene] += readcount
#let's get "per million" scaling factor:
per_mil_scal = float(nreads/1000000)

for key, value in cdict.items():
	if value > 0:
		rpm = float(value/per_mil_scal)
		medlen_kb = medlen_dict[key]/1000
		print (key, rpm/medlen_kb, samplename)
