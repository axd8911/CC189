def nextNumber(num1,num2):
	numString1 = list(str(num1))[::-1]
	numString2 = list(str(num2))[::-1]
	
	n = 0
	flips = 0
	while True:
		print (numString1[n], numString2[n])
		if numString1[n] != numString2[n]:
			
			flips = flips + 1
		n = n + 1	
		if len(numString1) == n and len(numString2) != n:
			numString1.append('0')
		if len(numString1) != n and len(numString2) == n:
			numString2.append('0')
	
		if len(numString1) == n and len(numString2) == n:
			break
			
	return flips
	
	
print (nextNumber(101101101,1111010010))
