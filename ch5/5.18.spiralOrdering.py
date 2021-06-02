def matrix_in_spiral_order(square_matrix):
    if not len(square_matrix):
        return []
    res = []
    left, top, right, bottom = 0, 0, len(square_matrix) - 1, len(square_matrix[0]) - 1
    print(left, top, right, bottom)
    while left <= right and top <= bottom:

        for i in range(left, right + 1):
            res.append(square_matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            res.append(square_matrix[i][right])
        right -= 1

        if top != bottom:
            for i in range(right, left - 1, -1):
                res.append(square_matrix[bottom][i])
            bottom -= 1

        if left != right:
            for i in range(bottom, top - 1, -1):
                res.append(square_matrix[i][left])
            left += 1
        
    return res

mat = ([[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]])

# print(matrix_in_spiral_order(mat))

mat = ([[1, 2 ], 
        [4, 5], ]
      )

mat = []

print(matrix_in_spiral_order(mat))