
import time

def collatz_sequence():
	a=[0,0]
	for n in range(1,1000000):
		ct= count(n)
		if ct>a[1]:
			a[0]=n
			a[1]=ct
	return a




def count(n):
	count=1
	while(n!=1):
		if n%2==0:n=n/2
		else: n=3*n+1
		count+=1
	return count
	
				
#print collatz_sequence()

#------------------------above is the easy solution with no optimizations----------------------------


#------------------------Now enhance the algorithm---------------------------------------------------

 
start = time.time()
 
limit = 1000000
collatz_length = [0] * limit
collatz_length[1] = 1
max_length = [1,1]
 
for i in range(1,1000000):
    n,s = i,0
    TO_ADD = [] # collatz_length not yet known
    while n > limit - 1 or collatz_length[n] < 1:
        TO_ADD.append(n)
        if n % 2 == 0: n = n/2
        else: n = 3*n + 1
        s += 1
    # collatz_length now known from previous calculations
    p = collatz_length[n]
    for j in range(s):
        m = TO_ADD[j]
        if m < limit:
            new_length = collatz_length[n] + s - j
            collatz_length[m] = new_length
            if new_length > max_length[1]: max_length = [i,new_length]
 
elapsed = (time.time() - start)
print "found %s at length %s in %s seconds" % (max_length[0],max_length[1],elapsed)

