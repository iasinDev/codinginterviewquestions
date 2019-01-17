def twins(a, b):
    result = []
    for i in range(len(a)):
        aEven, aOdd = [], []
        for j in range(len(a[i])):
            if j % 2 == 0:
                aEven.append(a[i][j])
            else:
                aOdd.append(a[i][j])
        aEven.sort()
        aOdd.sort()
        bEven,bOdd = [],[]
        for j in range(len(b[i])):
            if j%2==0:
                bEven.append(b[i][j])
            else:
                bOdd.append(b[i][j])
        bEven.sort()
        bOdd.sort()
        result.append("Yes" if aEven == bEven and aOdd == bOdd else "No")
    return result

print(twins(["cdab", "dcba", "abcd"],["abcd", "abcd", "abcdcd"]))
        
        
