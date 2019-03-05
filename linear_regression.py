import csv

def createMatrixes(filename):
	airfoil_file = open(filename, 'r')
	lines = airfoil_file.readlines()
	matrixA=[[0 for x in range(5)] for y in range(len(lines))]

	print(len(lines))

if __name__ == "__main__":
	createMatrixes("airfoil_train_.csv")

