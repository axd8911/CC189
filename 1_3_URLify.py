def URLify(strs,length):
	
	n = 1
	while n < len(strs):
		if strs[n] == ' ' and strs[n-1] == ' ':
			strs = strs[:n] + strs[n+1:]
		else: n = n + 1	
	strs = strs.replace(' ', '%20')
	return strs

def main():
	strs = '   '
	length = len(strs)
	a = URLify(strs,length)
	print ('a =',a, '/end')


main()
