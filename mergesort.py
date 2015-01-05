def msort2(x):
    if len(x) < 2:
        return x
    result = []          # moved!
    mid = int(len(x)/2)
    y = msort2(x[:mid])
    z = msort2(x[mid:])
    while (len(y) > 0) and (len(z) > 0):
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
    result += y
    result += z
    return result

A=[6,5,3,1,8,7,2,4]
print msort2(A)
