def flipBitToWin(num):
	numConvert = bin(num)
	print (numConvert)
	numString = list(str(numConvert))[2:]
	print (numString)
	a1 = 0
	a2 = 0
	a3 = 0
	max_gap = 0
	for i in range(len(numString)):
		if numString[i] == '0':
			a3 = i
			
			gap = a3 - a1 - 1
			if gap > max_gap:
				max_gap = gap
			print (i,a1,a2,a3,max_gap)
			a1 = a2
			a2 = a3
		
	
	if i - a1 > max_gap:
		return i - a1
	else:
		return max_gap
	
print (flipBitToWin(98875))

