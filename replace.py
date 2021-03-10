import os
import re

arr = os.listdir('/var/datastage/developers/Ayesha/MKTAP')
path = '/var/datastage/developers/Ayesha/MKTAP'
for file in arr:
	if '20210215' in file:
		nfile = file.replace('20210215','20210217')
		cmd = 'mv ' + path + '/' + file + ' ' + path + '/' + nfile
		os.system(cmd)
	fopen = open("/var/datastage/developers/Ayesha/MKTAP/"+file,'r')
	fwrite = open("/var/datastage/developers/Ayesha/MKTAP/"+file+"_bkpnb",'w')
	for line in fopen:
		alist = re.split(r'^[H]\|15022021\|',line)
		print(alist)
		if(len(alist) > 1):
			print('H|17022021|'+alist[1])
		 	fwrite.write('H|17022021|'+alist[1])
		else:
			fwrite.write(line)

	fopen.close()
	fwrite.close()
