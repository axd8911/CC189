def palindromePermutation(strs):
	strs.replace(' ','')
	
	dict_strs = {}
	
	for item in strs:
		if item in dict_strs:
			dict_strs[item] = dict_strs[item] + 1
		else:
			dict_strs[item] = 1
	
	n = 0
	for key in dict_strs:
		if dict_strs[key] % 2 == 1:
			n = n + 1
		if n == 2:
			return False
			
	return True

	
def main():
	strs = 'ab'
	a = palindromePermutation(strs)
	print (a)

main()
