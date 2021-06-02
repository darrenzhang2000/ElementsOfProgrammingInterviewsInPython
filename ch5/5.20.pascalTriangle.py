'''
1
1 1
1 2 1
1 3 3 1
1 4  6  4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
'''

def generatePascalTriangle(n):
    res = [[1] for _ in range(n)]
    for i in range(1, n):
        prevRow = res[i - 1]
        for j in range(1, len(prevRow)):
            res[i].append(prevRow[j - 1] + prevRow[j])
        res[i].append(1)
    return res

def generatePascalTriangle2(n):
    res = [[1] * (i + 1)  for i in range(n)]
    for i in range(1, n):
        prevRow = res[i - 1]
        for j in range(1, len(prevRow)):
            res[i][j] = prevRow[j - 1] + prevRow[j]
    return res

print(generatePascalTriangle2(7))