def Insertion(N,M,i,j):
	N_comp = list(str(N)[::-1])
	M_comp = list(str(M)[::-1])
	N_comp[i:i+len(M_comp)] = M_comp
	return ''.join(N_comp[::-1])
	
print (Insertion(10000000000,10011,2,6))
