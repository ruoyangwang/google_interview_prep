import math
def pythagorean():
	for c in range(334,998):
		for b in range(2,c):
			a=1000-c-b
			if a**2+b**2==c**2 and a<b:
					print a, b, c
					return None
		  
pythagorean()
