def msort(a):
	if len(a)<2:
		return a
	result=[]
	mid=int(len(a)/2)
	first= msort(a[:mid])
	second=msort(a[mid:])

	while(len(first)>0 and len(second)>0):

		if first[0]>second[0]:
			result.append(second[0])
			second.pop(0)
		else:
			result.append(first[0])
			first.pop(0)
	result+=second
	result+=first
	return result

A=[6,5,3,1,8,7,2,4]
print msort(A)
