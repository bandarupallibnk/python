import os
import sys
import string

def print_board(arr):
	for i in range(0,len(arr)):
		if i > 0:
			print('\n')
		txt = ''
		for j in range(0,len(arr[i])):
			txt = txt + str(arr[i][j]) + '\t'
		print(txt)

def player1():
	result = input('enter a value: ')
	print('This is the input ' + str(result))
	return result
#board([[1,2,3],[4,5,6],[7,8,9]])
print(player1())