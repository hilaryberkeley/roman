# This is a program which can be used to convert arabic to roman numerals, and reverse.

import sys
import math


NumMap = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5, 'VI':6, 'VII':7, 'VIII':8, 'IX':9, 'X':10,
'L':50, 'C':100, 'D':500, 'M':1000
}

arNum = int(raw_input('Please enter a zero to four digit number: ')[:4])
lengarNum = len(str(arNum))
# print lengarNum


if lengarNum == 1:
	def find_key(NumMap, arNum):
		for k, v in NumMap.items():
			if v == arNum:
				yield k
				print next(find_key(NumMap, 'arNum'), None)

	# if arNum in NumMap:
	# 	print key
	# 	print 'Your roman numeral is: %s', % NumMap[arNum]

else:
	print "whatever"



# elif len(arNum) = 2:

# elif len(arNum) = 3:
# elif len(arNum) = 4: