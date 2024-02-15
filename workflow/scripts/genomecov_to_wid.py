import sys
#input: .bgcov file created as an output of bedtools genomecov (short format)
with open(sys.argv[1]) as file:
	f = file.read().split('\n')[:-1]

dct_cov = {}
dct_len = {}
for i in f:
	temp = i.split('\t')
	#ignoring non-informative last lines of the file
	if not temp[0] == "genome":
		name = temp[0]
		cov = int(temp[1])
		if not cov == 0:
			#store the number of covered bases in a dictionary
			if not name in dct_cov:
				dct_cov[name] = int(temp[2])
				dct_len[name] = int(temp[3])
			else:
				dct_cov[name] += int(temp[2])
for key,value in dct_cov.items():
	#report covered bases as in % of a sequence length
	print (key, value*100/dct_len[key], dct_len[key])
