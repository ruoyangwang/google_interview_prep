import urllib2
file_url = 'https://projecteuler.net/project/resources/p081_matrix.txt'
matrix = [[int(n) for n in s.split(',')] for s in urllib2.urlopen(file_url).readlines()]

def minimal_path_sum():
	size = len(matrix)
  # calculate minimal sums for bottom row and last column
  # as they don't have any other way to be reached
  	for i in reversed(range(0, size - 1)):
		matrix[size - 1][i] += matrix[size - 1][i + 1]
		matrix[i][size - 1] += matrix[i + 1][size - 1]


	for i in reversed(range(0, size - 1)):
		for j in reversed(range(0, size - 1)):
		  	matrix[i][j] += min(matrix[i + 1][j], matrix[i][j + 1])

	return matrix[0][0]

print minimal_path_sum()
