import urllib2
 
file_url = 'https://projecteuler.net/project/resources/p067_triangle.txt'
table = [[int(n) for n in s.split()] for s in urllib2.urlopen(file_url).readlines()]
 
for row in reversed(range(1,len(table))):
    for col in range(0, row):
        table[row-1][col] += max(table[row][col], table[row][col+1])
 
print "Project Euler 67 Solution =", table[0][0]
	
