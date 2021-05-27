'''
can reach end of array.

input:
[3, 3, 1, 0, 2, 0, 1]

output:
true
index 0, index 1, index 4, end

[3, 3, 1, 0, 2, 0, 1]
stepsLeft = arr[0]
maxReach = arr[0]

'''

def canReachEnd(arr):
    maxReach = arr[0]
    idx = 0
    while idx <= maxReach and idx < len(arr):
        maxReach = max(maxReach, idx + arr[idx])
        if maxReach >= len(arr) - 1:
            return True
        idx += 1
    return False

arr = [3, 3, 1, 0, 2, 0, 1]
print(canReachEnd(arr))
arr = [1, 0, 0]
print(canReachEnd(arr))
arr = [1]
print(canReachEnd(arr))
