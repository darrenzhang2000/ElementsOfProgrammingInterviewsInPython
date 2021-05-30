'''
same as randomSampling except size of arr keeps increasing
'''

from randomSample import randomSample

arr = [1, 2, 3, 4, 5, 6]
k = 4
def onlineRandomSample(): # time O(nk) where n is the number of input elements
    k = int(input("enter k: "))
    n = None
    arr = []
    while n != "quit":
        n = input("element to insert or type quit to exit: ")
        arr.append(n)
        if len(arr) < k: 
            print(randomSample(arr, len(arr)))
        else:
            print(randomSample(arr, k))


# onlineRandomSample()
import itertools
import random
# assume at least k elements
def onlineRandomSample2(stream, k): # O(n) time
    runningSample = list(itertools.islice(stream, k))
    numSeenSoFar = k
    for x in stream:
        numSeenSoFar += 1
        idxToReplace = random.randrange(numSeenSoFar)
        if idxToReplace < k:
            runningSample[idxToReplace] = x
        print(runningSample)
    return runningSample

arr = [1, 2, 3, 4, 5, 6, 7]
it = iter(arr)
onlineRandomSample2(it, 4)