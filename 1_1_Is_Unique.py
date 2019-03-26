'''
what is the time complexicity of "not in"?
One tip asks to make it n.logn


'''


def isUnique(strs):

	n = 1
	for item in strs:
		if item not in strs[:n-1]:
			n = n + 1
		else:
			return False		
	return True


def main():
	strs = 'qwertyuiop[['
	output = isUnique(strs)
	print (output)


main()
