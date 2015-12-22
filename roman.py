# This is a program which can be used to convert arabic to roman numerals, and reverse.
# Due to the "bar" symbol on Roman numerals 4,000 and up, I limited this to 3,999.

# Roman Numeral Array
RomArray = ['MMM', 'MM', 'M', 'CM', 'DCCC', 'DCC', 'DC', 'D', 'CD', 'CCC', 'CC', 'C', 
			'XC', 'LXXX', 'LXX', 'LX', 'L', 'XL', 'XXX', 'XX', 'X', 'IX', 'VIII', 
			'VII', 'VI', 'V', 'IV', 'III', 'II', 'I']

# Arabic Numeral Array
AraArray = [3000, 2000, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 90, 80, 70, 60,
			50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

MIN_NUM = 1
MAX_NUM = 3999

def arabic_to_roman(ar_num):
	numeral = ''
	for i, v in enumerate(AraArray):
		into = ar_num / v
		if into == 1:
			numeral += RomArray[i]
			remainder = ar_num - v
			ar_num = remainder	
	return numeral

# Get a four digit Arabic Numeral from a user, convert it to a Roman Numeral
u_arabic = raw_input('Please enter a number between %d and %d: ' % (MIN_NUM, MAX_NUM))
u_arabic = int(u_arabic)
if u_arabic > MAX_NUM:
	quit('%d is too big. Please try again.' % u_arabic)
elif u_arabic < MIN_NUM:
	quit('%d is too small.  Please try again.' % u_arabic)


print "Your Roman numeral is: " + arabic_to_roman(u_arabic)

print '-' * 40

# Get a Roman Numeral from a user, convert it to an Arabic Numeral
u_roman = raw_input('Please enter a Roman Numeral whose Arabic Numeral value is between %d and %d: ' % (MIN_NUM, MAX_NUM))


def roman_to_arabic(ro_num):
	numeral = int()
	for i, v in enumerate(RomArray):
		if ro_num.startswith(v):
			numeral += AraArray[i]
			ro_num = ro_num[len(v):]
		if numeral == 0:
			numeral = 'not between %d and %d.  Please try again. ' % (MIN_NUM, MAX_NUM)
	return numeral

print "Your Arabic Numeral is: " + str(roman_to_arabic(u_roman))

