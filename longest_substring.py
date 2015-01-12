string1 = "abcdefghijklmnopqrstuvwxyz"
string2 = "111ijklmno1111klmnopqrstuvwxyz1111111wxy111111"
#Make sure string 1 is the shorter string, to be more efficient
if len(string1)>len(string2):
    string1, string2 = string2, string1
substr = ""
#Loop through each possible start for a substring
for start in range(len(string1)):
    #Loop through each possible ending for the current start
    for end in range(start,len(string1)):
        sub = string1[start:end+1]
        #if it's in the other string, it's common
        if sub in string2:
            #if it's longer than the current longest common substring found
            if len(sub)>len(substr):
                #it's the new longest common substring
                substr = sub
        #otherwise, this start is wrong, move on to the next start
        else:
            break
print substr
