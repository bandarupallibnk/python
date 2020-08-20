from bullet import bullet
from edate import cl_date
import sys
import os


 
units = int(sys.argv[1])
start = int(sys.argv[2])
size = int(sys.argv[3])
rounds = 10000
maxbsize = units*8
dt = cl_date()
stoday = dt.fcurrentdate()
fpath = '/Users/nandabandarupalli/Documents/python/seqdata/' + stoday + '.txt'
try:
	os.remove(fpath)
except:
	pass

#def __init__(self,units,start,size,rounds,fpath):

#Main function which calls teh logic
if __name__=='__main__':
	objseq = bullet(units,start,size,rounds,fpath)
	for i in range(1,rounds):
		vallist = objseq.gen_list()  # Generates the list
		#print(vallist) 
		blist = objseq.identify_1_12(vallist) # Identifies the if within range
		#print(blist)
		objseq.repeated(blist) # Identify number of times repeated
		#writedouble('Game' + str(i) ,blist)
		objseq.writeseq('Game' + str(i), blist)
		#writeodd('Game' + str(i), blist)
		print(i)
		#blist = identify_1_12(vallist)