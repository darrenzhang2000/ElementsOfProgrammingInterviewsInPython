from randomSample import randomSample

def generateRandomPermutation(n):
    permutations = list(range(n))
    randomSample(permutations, n)
    return permutations

print(generateRandomPermutation(7))