'''
How to convert decimal (0,1) to binary? This question gives an answer 
'''

def binaryToString(number):
	result = ['0.']
	while number != 0:
		number = number * 2
		if number >= 1:
			number = number - 1
			result.append(str(1))
		else:
			result.append(str(0))
			
		if len(result) == 33:
			return 'ERROR'
			
	return ''.join(result)
		
print (binaryToString(0.8125))
