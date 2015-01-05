import math
def difference(n):
	return int(math.fabs(reduce(lambda x,y:x+y, map(lambda x:x**2,range(1,n+1)))-(reduce(lambda x,y:x+y, range(n+1)))**2))



print difference(3)
