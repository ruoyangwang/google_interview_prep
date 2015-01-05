def quicksort(a):
	if len(a)<2:
		return a
	pivot= a[0]
	less=[i for i in a if i<pivot]
	eql=[i for i in a if i==pivot]
	gtr=[i for i in a if i>pivot]
	return quicksort(less)+eql+quicksort(gtr)

A=[6,5,3,1,8,7,2,4]
print quicksort(A)
