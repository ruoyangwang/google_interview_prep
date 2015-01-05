module_factor=10**10

def self_power(n):
	global module_factor
	sum=0
	for i in range(n+1):
		sum+=(i**i)%module_factor
	return sum%module_factor

print self_power(1000)
