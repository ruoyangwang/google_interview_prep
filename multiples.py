def multiples(n):
	retval=0
	for i in range(n):
		if i%3==0 or i%5==0:
			retval+=i
	return retval

print multiples(10)
