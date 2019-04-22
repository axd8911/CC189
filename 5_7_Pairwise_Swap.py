def pairwiseSwap(num):
	numString = list(str(num))
	
	if len(numString)%2 == 1:
		numString.insert(0,'0')		
	for i in range(int(len(numString)/2)):
		numString.insert(2*i+1,numString.pop(2*i))
		
	return ''.join(numString)
	
print (pairwiseSwap(123987654))
