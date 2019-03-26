def oneAway(str1, str2):

	if abs(len(str1) - len(str2)) > 1:
		return False
		
	n = 0
	
	while n < len(str1):
		if str1[n] == str2[n]:
			n = n + 1
			continue
		if len(str1) == len(str2):
			str1 = str1[:n] + str1[n+1:]
			str2 = str2[:n] + str2[n+1:]
		if len(str1) > len(str2):
			str1 = str1[:n] + str1[n+1:]
		if len(str2) > len(str1):
			str2 = str2[:n] + str2[n+1:]
			
		if str1 != str2:
			return False
			
	return True

	
def main():
	str1 = 'qwerta '
	str2 = 'qwera '
	a = oneAway(str1, str2)
	print (a)

main()
