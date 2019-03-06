import csv

def createMatrixes(filename):
	airfoil_file = open(filename, 'r')
	lines = airfoil_file.readlines()
	#matrices y vectores
	matrixA=[[0 for x in range(5)] for y in range(len(lines))]
	matrixAT = [[0 for x in range(len(lines))] for y in range(5)]
	resultVector =[len(lines)]

	for currentLine in range(len(lines)):
		temporary = lines[currentLine].split()
		resultVector.append(temporary.pop())
		matrixA[currentLine] = temporary
		for x in range(5):
			matrixAT[x][currentLine] = temporary[x]

	
	return matrixA, matrixAT, resultVector


def matrixMultiplier(A, BT):
	print(len(A))
	print(len(BT[0]))
	if(type(BT[0]) is not list):
		if(len(A) != len(BT)):
			print("las matrices no se pueden multiplicar")
			return 0

	else:
		if(len(A) != len(BT[0])):
			print("Las matrices no se pueden multiplicar")
			return 0

	resultMatrix = [[0 for x in range(len(BT))] for y in range(len(A[0]))]
	for i in range(len(BT)):
   		for j in range(len(A[0])):
   			for k in range(len(A)):
   				resultMatrix[i][j] += float(BT[i][k]) * float(A[k][j])

	return resultMatrix


if __name__ == "__main__":
	A, AT, resultVector = createMatrixes("airfoil_train_.csv")
	resultMatrix = matrixMultiplier(A,AT)
	finalVector = matrixMultiplier(AT, resultVector)



