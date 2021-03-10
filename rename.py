import os
import re

arr = os.listdir('/var/datastage/developers/Ayesha/MKTAP')
path = '/var/datastage/developers/Ayesha/MKTAP'
for file in arr:
	if '_bkpnb' in file:
		nfile = file.replace('_bkpnb','')
		cmd = 'mv ' + path + '/' + file + ' ' + path + '/' + nfile
		os.system(cmd)
