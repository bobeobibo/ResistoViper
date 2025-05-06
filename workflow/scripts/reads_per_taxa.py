import sys
import os
#first kraken report, next nreads file
with open(sys.argv[2]) as file0:
	allreads = float(file0.read().split('\n')[0].split(' ')[0])
pmscale = allreads/1000000
with open(sys.argv[1]) as file:
	f = file.read().split('\n')[5:-1] #here we cut the header starting with "#"
for i in f:
	temp = i.split('\t') #pay attention to separators, they used to be different
	taxon = temp[0].replace(" ","_").replace("'","")
	nreads = float(temp[1])
	#add "million" scaling factor
	rpm = nreads/pmscale
	print (taxon, rpm, pmscale, os.path.basename(str(sys.argv[2])[:-7]))
#print (allreads)
