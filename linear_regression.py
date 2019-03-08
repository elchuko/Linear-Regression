import csv
import math
import gauss_jordan as gj

def createMatrixes(filename):
	airfoil_file = open(filename, 'r')
	lines = airfoil_file.readlines()
	#matrices y vectores
	matrixA = [[0 for x in range(5)] for y in range(len(lines))]
	matrixAT = [[0 for x in range(len(lines))] for y in range(5)]
	resultVector =[]

	for currentLine in range(len(lines)):
		temporary = lines[currentLine].split()
		#resultVector.append(temporary[len(temporary)-1])
		resultVector.append(temporary.pop())
		matrixA[currentLine] = temporary
		for x in range(5):
			matrixAT[x][currentLine] = temporary[x]

	
	return matrixA, matrixAT, resultVector

def addRowOfOnes(matrix):
	row = [1 for i in range(len(matrix[0]))]
	matrix.insert(0, row)
	return matrix;
	

def addColumnOfOnes(matrix):
	for i in range(len(matrix)):
		matrix[i].insert(0,1)

	return matrix;


def matrixMultiplier(A, BT):
	if(type(BT[0]) is not list):
		if(len(A[0]) != len(BT)):
			print("las matrices no se pueden multiplicar")
			return 0
		else:
			resultMatrix = [0 for y in range(len(A))]
			for i in range(len(A)):
				for j in range(len(BT)):
					resultMatrix[i] += float(A[i][j]) * float(BT[j])
					
	else:
		if(len(A) != len(BT[0])):
			print("Las matrices no se pueden multiplicar")
			return 0
		else:
			resultMatrix = [[0 for x in range(len(BT))] for y in range(len(A[0]))]
			for i in range(len(BT)):
				for j in range(len(A[0])):
					for k in range(len(A)):
						resultMatrix[i][j] += float(BT[i][k]) * float(A[k][j])

	return resultMatrix

def joinMatrixes(matrix, result):
	for i in range(len(matrix)):
		matrix[i].append(result[i])
	return matrix

def splitMatrix(matrix):
	resultVector = []
	for i in range(len(matrix)):
		resultVector.append(matrix[i].pop())

	return resultVector

def calculateRMSE(matrix,yVector,values):
	resultV = [values[0] for i in range(len(yVector))]
	values.pop(0)
	for height in range(len(matrix)):
		for width in range(len(matrix[0])):
			print("resultV={} matrix={} values={}",resultV[height],matrix[height][width],values[width])
			resultV[height] += float(matrix[height][width])*float(values[width])
	
	RMSE = float(0)
	for i in range(len(resultV)):
		RMSE += (float(resultV[i])-float(yVector[i]))**2

	RMSE = math.sqrt(RMSE/len(resultV))
	return RMSE

	

if __name__ == "__main__":
	A, AT, resultVector = createMatrixes("airfoil_train_.csv")
	A1 = addColumnOfOnes(A)
	AT1 = addRowOfOnes(AT)
	resultMatrix = matrixMultiplier(A1,AT1)
	finalVector = matrixMultiplier(AT1, resultVector)
	values = splitMatrix(gj.gauss_jordan(joinMatrixes(resultMatrix,finalVector)))
	testMatrix, AT, resultVector = createMatrixes("airfoil_test_.csv")
	print(calculateRMSE(testMatrix,resultVector,values))
	


	
	



