def zeroMatrix(matrix):

	flag = 1
	for item in matrix:
		if 0 in item:
			flag = 0
			break
			
	if flag == 0:
		matrix = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
	
	return matrix
		
def main():
	matrix = [[0,1,2,3],[3,4,5,6],[6,7,8,9]]
	a = zeroMatrix(matrix)
	print (a)

main()
