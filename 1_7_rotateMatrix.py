'''
Almost the same as LC048
'''

def rotateMatrix(matrix):

	print (matrix[1])
	matrix = [[matrix[x][y] for x in range(len(matrix))] for y in range(len(matrix)-1,-1,-1)]
	return matrix
		
def main():
	matrix = [[0,1,2],[3,4,5],[6,7,8]]

	a = rotateMatrix(matrix)
	print (a)

main()
