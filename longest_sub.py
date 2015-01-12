def longest_substr(s1,s2):
	longest=""
	if len(s2)>len(s1):
		s1,s2=s2,s1
	for head in range(len(s1)):
		for tail in range(head+1,len(s1)):
			if s1[head:tail] in s2:
				if len(s1[head:tail])>len(longest):
					longest=s1[head:tail]
	return longest


s1='abcdefg'
s2='defabcg'
print longest_substr(s1,s2)
				
