from typing import List
import math

def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    def hasDuplicate(block):
        filteredBlock = list(filter(lambda x: x != 0, block))
        return len(filteredBlock) != len(set(filteredBlock))

    n = len(partial_assignment)

    # if any rows have duplicates
    if any([hasDuplicate(row) for row in partial_assignment]): 
        return False

    # if any columns have duplicates
    if any(hasDuplicate([partial_assignment[i][j] 
        for i in range(n)]) 
        for j in range(n)
    ):
        return False

    def isValidGrid(mat, startR, startC):
        return not hasDuplicate(partial_assignment[i][j] 
            for i in range(startR, startR + 3) 
            for j in range(startC, startC + 3)
        )

    regionSize = int(math.sqrt(n))

    return all(isValidGrid(partial_assignment, startR, startC) 
        for startR in range(0, n, regionSize) 
        for startC in range(0, n, regionSize)
    )