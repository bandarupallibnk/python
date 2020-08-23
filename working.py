import os


fopen = open("/Users/nandabandarupalli/pkgs.txt","r")
fwrite = open("/Users/nandabandarupalli/res.sh","w")
for line in fopen:
	cmd = "pip uninstall " + line
	fwrite.write(cmd)

fopen.close()
fwrite.close()