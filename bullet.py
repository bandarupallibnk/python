import os
import sys
import time
import random
import datetime
from edate import cl_date

class bullet():

	def __init__(self,units,start,size,rounds,fpath):
		self.units = units
		self.start = start
		self.size = size
		self.rounds = rounds
		self.fpath = fpath
		self.maxbsize = self.units*8
		self.dt = cl_date()
		self.stoday = self.dt.fcurrentdate()



	# Generate Random lists
	def gen_list(self):
	#	nums = [9, 28, 0, 12, 26, 25, 23, 35, 29, 33, 37, 35, 24, 9, 8, 19, 2, 1, 4, 1]
		nums = []
		for i in range(0,self.size):
			nums.append(random.randint(0,37))
		return nums

	# Identify if the numbers are between 1 and 12
	def identify_1_12(self,arr):
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

	def identify_even_odd(self,arr):
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
	def repeated(self,blist):
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
	def roll(self,finval,activeval):
		return finval-activeval

	#Set max bet size
	def setmaxbsize(self,activeval):
		activeval = activeval*2
		if activeval > self.maxbsize:
			return self.maxbsize
		else:
			return activeval

	def printformat(self,curround,i,binval,activeval,result,finval):
		output = curround + "\t" +  str(i) + "\t" +  str(binval) + "\t" + str(activeval) + "\t" + str(result) + "\t" + str(finval) + "\n"
		print (output)
		return output

	#Increment self.units by multiple of self.units like 10,20,40,80
	def calculatedouble(self,curround,blist,fpath):
		activeval = self.units
		result = 1
		finval = self.start
		fdouble = open(fpath,'a')
		for i in range(0,self.size):
			finval = self.roll(finval,activeval)
			if blist[i] == -1:
				result = activeval*0  
				finval = finval + result
				#print(str(blist[i]) + "\t" + str(activeval) + "\t" + str(result) + "\t" + str(finval))
				fdouble.write(printformat(curround,i,blist[i],activeval,result,finval))
				activeval = int(activeval/2)
				if(activeval < self.units):
					activeval = self.units
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
	def calculateadd(self,curround,blist,fpath):
		activeval = self.units
		result = 1
		finval = self.start
		fseq = open(fpath,'a')
		for i in range(0,self.size):
			finval = self.roll(finval,activeval)
			if blist[i] == -1:
				result = activeval*0
				finval = finval + result
				fseq.write(self.printformat(curround,i,blist[i],activeval,result,finval))
				activeval =  activeval - self.units
				if(activeval < self.units):
					activeval = self.units
			elif blist[i] == blist[i-1] == 1:
				result = activeval*3
				finval = finval + result 
				fseq.write(self.printformat(curround,i,blist[i],activeval,result,finval))
				activeval = activeval + self.units
			elif blist[i] == 1:
				result = activeval*3
				finval = finval + result 
				fseq.write(self.printformat(curround,i,blist[i],activeval,result,finval))
				activeval = activeval + self.units

	#Increment units by adding units sequentially like 10,20,30,40
	def calculateadd_odd(self,curround,blist,fpath):
		activeval = self.units
		result = 1
		finval = self.start
		fseq = open(fpath,'a')
		for i in range(0,size):
			finval = roll(finval,activeval)
			if blist[i] == -1:
				result = activeval*0
				finval = finval + result
				fseq.write(printformat(curround,i,blist[i],activeval,result,finval))
				activeval =  activeval - int(activeval/2)
				if(activeval < self.units):
					activeval = self.units
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
			if (activeval > self.maxbsize):
				activeval = self.maxbsize
			
	def writedouble(self,curround,blist):
		fpath = '/Users/nandabandarupalli/Documents/python/doubledata/' + stoday + '.txt'
		calculatedouble(curround,blist,fpath) 

	def writeseq(self,curround,blist):
		self.calculateadd(curround,blist,self.fpath)

	def writeodd(self,curround,blist):
		fpath = '/Users/nandabandarupalli/Documents/python/seqodd/' + stoday + '.txt'
		calculateadd_odd(curround,blist,fpath)


	#Main function which calls teh logic
	if __name__=='__main__':
		for i in range(1,self.rounds):
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