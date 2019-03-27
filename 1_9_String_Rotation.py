def stringRotation(s1,s2):

	if s1 == s2[::-1]:
		return True
	else: return False
	
		
def main():
	s1 = 'abcde'
	s2 = 'edcbb'

	a = stringRotation(s1,s2)
	print (a)

main()
