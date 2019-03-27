def stringCompression(strs):
	if strs == '':
		return ''
	
	shorter = []
	shorter.append(strs[0])
	count = 1
	
	for i in range(1,len(strs)):
		if strs[i] == strs[i-1]:
			count = count + 1
		if strs[i] != strs[i-1]:
			shorter.append(str(count))
			count = 1
			shorter.append(strs[i])
			
	shorter.append(str(count))
			
	if len(shorter) < len(strs):
		return ''.join(shorter)
		
	else: return strs
			
def main():
	strs = 'aaaaabc'

	a = stringCompression(strs)
	print (a)

main()
