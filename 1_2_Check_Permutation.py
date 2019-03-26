
def checkPermutation(strs1,strs2):

	dict_strs1 = {}
	dict_strs2 = {}
	
	for item in strs1:
		if item in dict_strs1:
			dict_strs1[item] = dict_strs1[item] + 1
		else:
			dict_strs1[item] = 1
			
	for item in strs2:
		if item in dict_strs2:
			dict_strs2[item] = dict_strs2[item] + 1
		else:
			dict_strs2[item] = 1
			
	if dict_strs1 == dict_strs2:
		return True
		
	else: return False

def main():
	strs1 = 'qwertyufghhaabaiop[['
	strs2 = 'hhqfw[eart[yuioaagp'
	output = checkPermutation(strs1, strs2)
	print (output)

main()
