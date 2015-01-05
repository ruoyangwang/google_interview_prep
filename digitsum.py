
#---------------------dumb way---------------------

def digit_sum(n):
	result=str(2**n)
	digitsum=0
	for i in result:
		digitsum+=int(i)
	return digitsum


print digit_sum(15)


#---------------------shorter way-----------------
def digit_sum_short(n):
	return reduce(lambda x,y:int(x)+int(y), str(2**n))

print digit_sum_short(15)


#---optimized way i guess is to cache all calculated result into a dictionary, then do lookup----
