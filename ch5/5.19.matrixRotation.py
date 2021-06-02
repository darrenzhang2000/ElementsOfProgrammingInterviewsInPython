'''
rotate matrix 90 degrees
[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10,11,12],
    [13,14,15,16]
]

[
    [1, 2, 3, 1],
    [5, 6, 7, 2],
    [9, 10,11,3],
    [13,14,15,4]   
]

curEdge = [1, 2, 3, 4]
nextEdge = [4, 8, 12, 16]
updateNextEdge
curEdge = nextEdge -> [4, 8, 12, 16]

curEdge = [4, 8, 12, 16]
nextEdge = 
'''

# brute force
def matrixRotation(mat):
    newMat = [[None for _ in mat] for _ in mat[0]]
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            newX, newY = y, len(mat) - 1 - x
            newMat[newX][newY] = mat[x][y]
    return newMat

def inBounds(mat, x, y):
    if not len(mat):
        return False
    return 0 <= x < len(mat) and 0 <= y < len(mat[0])

def matrixRotation2(mat):
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = x = y = 0
    while True:
        curVals = []
        nextX, nextY = x + directions[direction][0], y + directions[direction][1]
        while inBounds(mat, nextX, nextY):
            nextX, nextY = x + directions[direction][0], y + directions[direction][1]
            curVals.append(mat[x][y])
            if inBounds(mat, nextX, nextY):
                x, y = nextX, nextY

        nextDirection = (direction + 1) % 3
        direction = nextDirection
        nextVals = []
        nextX, nextY = x + directions[direction][0], y + directions[direction][1]
        print(x,y,nextX,nextY)
        i = 0
        while inBounds(mat, nextX, nextY):
            nextX, nextY = x + directions[direction][0], y + directions[direction][1]
            nextVals.append(mat[x][y])
            if i < len(curVals) - 1:
                mat[x][y] = curVals[i]
                i += 1
            if inBounds(mat, nextX, nextY):
                x, y = nextX, nextY



        print(curVals, nextVals, mat)
        return

def matrixRotation3(mat):
    for x in range(len(mat) // 2):
        for y in range(len(mat) - 1 - x):
            (mat[x][y], mat[~x][y], mat[~x][~y], mat[x][~y]) = (mat[y][~x], mat[y][x], mat[~y][x], mat[~y][~x])
            # mat[x][y] = mat[~x][y]
            # mat[~x][y] = mat[~x][~y]
            # mat[~x][~y] = mat[x][~y]
            # mat[x][~y] = temp
    print(mat)

mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10,11,12],
    [13,14,15,16]
]

print(matrixRotation3(mat))