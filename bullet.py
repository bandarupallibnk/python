import os
import sys
import time
import random
import datetime
from edate import cl_date


units = int(sys.argv[1])
start = int(sys.argv[2])
size = int(sys.argv[3])
rounds = 100
maxbsize = units*8
dt = cl_date()
print(dt)
stoday = dt.fcurrentdate()

# Generate Random lists
def gen_list():
#	nums = [9, 28, 0, 12, 26, 25, 23, 35, 29, 33, 37, 35, 24, 9, 8, 19, 2, 1, 4, 1]
	nums = []
	for i in range(0,size):
		nums.append(random.randint(0,37))
	return nums
# Identify if the numbers are between 1 and 12
def identify_1_12(arr):
	binarylist = []
	times = 0
	for val in arr:
		if val in range(1,13):
			binarylist.append(1)
			times = times + 1
		else:
			binarylist.append(-1)
	print('Number of times number has arrived {}'.format(times))
	return binarylist

def identify_even_odd(arr):
	binarylist = []
	times = 0
	for val in arr:
		if val%2 == 1:
			binarylist.append(1)
			times = times + 1
		else:
			binarylist.append(-1)
	print('Number of times odd number has arrived {}'.format(times))
	return binarylist

# Get count of times the sequence has been repeated
def repeated(blist):
	repeatcount = 0
	repeatmax = 0
	for i in range(0,len(blist)):
		if blist[i] ==  1 :
			repeatcount = repeatcount + 1
		elif blist[i] == -1:
			if repeatcount > repeatmax:
				repeatmax = repeatcount
			repeatcount  = 0
	if repeatcount > repeatmax:
		repeatmax = repeatcount
	print('The repeat count is {}'.format(repeatmax))

# Deduct everytime before counting
def roll(finval,activeval):
	return finval-activeval

#Set max bet size
def setmaxbsize(activeval):
	activeval = activeval*2
	if activeval > maxbsize:
		return maxbsize
	else:
		return activeval

def printformat(curround,i,binval,activeval,result,finval):
	output = curround + "\t" +  str(i) + "\t" +  str(binval) + "\t" + str(activeval) + "\t" + str(result) + "\t" + str(finval) + "\n"
	print (output)
	return output

#Increment units by multiple of units like 10,20,40,80
def calculatedouble(curround,blist,fpath):
	activeval = units
	result = 1
	finval = start
	fdouble = open(fpath,'a')
	for i in range(0,size):
		finval = roll(finval,activeval)
		if blist[i] == -1:
			result = activeval*0  
			finval = finval + result
			#print(str(blist[i]) + "\t" + str(activeval) + "\t" + str(result) + "\t" + str(finval))
			fdouble.write(printformat(curround,i,blist[i],activeval,result,finval))
			activeval = int(activeval/2)
			if(activeval < units):
				activeval = units
		elif blist[i] == blist[i-1] == 1:
			result = activeval*3
			finval = finval + result 
			fdouble.write(printformat(curround,i,blist[i],activeval,result,finval))
			activeval = setmaxbsize(activeval)
		elif blist[i] == 1:
			result = activeval*3
			finval = finval + result 
			fdouble.write(printformat(curround,i,blist[i],activeval,result,finval))
			activeval = setmaxbsize(activeval)

#Increment units by adding units sequentially like 10,20,30,40
def calculateadd(curround,blist,fpath):
	activeval = units
	result = 1
	finval = start
	fseq = open(fpath,'a')
	for i in range(0,size):
		finval = roll(finval,activeval)
		if blist[i] == -1:
			result = activeval*0
			finval = finval + result
			fseq.write(printformat(curround,i,blist[i],activeval,result,finval))
			activeval =  activeval - units
			if(activeval < units):
				activeval = units
		elif blist[i] == blist[i-1] == 1:
			result = activeval*3
			finval = finval + result 
			fseq.write(printformat(curround,i,blist[i],activeval,result,finval))
			activeval = activeval + units
		elif blist[i] == 1:
			result = activeval*3
			finval = finval + result 
			fseq.write(printformat(curround,i,blist[i],activeval,result,finval))
			activeval = activeval + units

#Increment units by adding units sequentially like 10,20,30,40
def calculateadd_odd(curround,blist,fpath):
	activeval = units
	result = 1
	finval = start
	fseq = open(fpath,'a')
	for i in range(0,size):
		finval = roll(finval,activeval)
		if blist[i] == -1:
			result = activeval*0
			finval = finval + result
			fseq.write(printformat(curround,i,blist[i],activeval,result,finval))
			activeval =  activeval - int(activeval/2)
			if(activeval < units):
				activeval = units
		elif blist[i] == blist[i-1] == 1:
			result = activeval*2
			finval = finval + result 
			fseq.write(printformat(curround,i,blist[i],activeval,result,finval))
			activeval = activeval + int(result/2)
		elif blist[i] == 1:
			result = activeval*2
			finval = finval + result 
			fseq.write(printformat(curround,i,blist[i],activeval,result,finval))
			activeval = activeval + int(result/2)
		if (activeval > maxbsize):
			activeval = maxbsize
		
def writedouble(curround,blist):
	fpath = '/Users/nandabandarupalli/Documents/python/doubledata/' + stoday + '.txt'
	calculatedouble(curround,blist,fpath) 

def writeseq(curround,blist):
	fpath = '/Users/nandabandarupalli/Documents/python/seqdata/' + stoday + '.txt'
	calculatedouble(curround,blist,fpath)

def writeodd(curround,blist):
	fpath = '/Users/nandabandarupalli/Documents/python/seqodd/' + stoday + '.txt'
	calculateadd_odd(curround,blist,fpath)


#Main function which calls teh logic
if __name__=='__main__':
	for i in range(1,rounds):
		vallist = gen_list()  # Generates the list
		print(vallist) 
		blist = identify_even_odd(vallist) # Identifies the even/odd
		print(blist)
		repeated(blist) # Identify number of times repeated
		#writedouble('Game' + str(i) ,blist)
		#writeseq('Game' + str(i), blist)
		writeodd('Game' + str(i), blist)
		print(i)
		blist = identify_1_12(vallist)