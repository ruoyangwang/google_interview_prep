collection=[2,3,5,7,11,13,17]
total_sum=0

def is_divisible(number):
	for i in range(len(collection)):
		digit_to_check=number[i+1:i+4]
		#print digit_to_check
		if int(digit_to_check) % collection[i]!=0:
			return False
	return True


def generate_num():
	global total_sum
	perm_number='0123456789'
	for instance in all_perms(perm_number):
		if instance[0]!='0' and is_divisible(instance):
			total_sum+=1
	return total_sum 
	

def all_perms(numstr):
	if len(numstr)==1:
		yield numstr
	else:
		for perms in all_perms(numstr[1:]):
			for i in range(len(perms)+1):
				yield perms[i:]+numstr[0]+perms[:i]
	



print generate_num()
