'''
Sample input: 
papers = [A, B, C, D, E, F, G, H, I]
citationCounts = [1, 4, 1, 4, 2, 1, 3, 5, 6]

Sample Output: 4 - (B, D, H, I)

Find the h-index of a researcher. H-index is the largest number h such that the researcher has published
h papers that habe been cited at least h times.

Brute force: 

start i = 0 and keep incrementing by 1:
    - for each i, loop through the papers. count paper with score > i
    - break and return i when count < i

Time: O(n^2), where n is len(papers). 
    - bounded by n. i can't be greater than n.

Space: O(1)

Bottle neck - having to go through the papers twice.

Optimizations:
    - sorting? 
        length = 9
        [1, 1, 1, 2, 3, 4, 4, 5, 6]
        h-value = 1 -> index of 1 is at 0. 9 - 0 = 9 elements >= 1. Continue.
        h-value = 2 -> index of 2 is at 3. 9 - 3 = 6 elements >= 2. Continue.
        h-value = 3 -> index of 3 is at 4. 9 - 4 = 5 elements >= 3. Continue.
        h-value = 4 -> index of 4 is at 5. 9 - 5 = 4 elements >= 4. Continue.
        h-value = 5 -> index of 5 is at 8. 9 - 8 = 1 element >= 5. Not enough elements. 
        Return i - 1 = 4.
        
        time: O(nlog) because we have to sort the array of papers. 
        space: O(n)
    
    - heap?
        heapify takes O(n) time. 
        h_index = 1 -> keep popping 1s ... not useful

    - stack - not useful
'''

def findHIndex(citations):
    citations.sort()
    length = len(citations)
    h_index = 1
    idx = 0
    while True:
        while idx < len(citations) and citations[idx] < h_index:
            idx += 1
        if not length - idx >= h_index:
            break
        h_index += 1
    return h_index - 1

print(findHIndex([1, 4, 1, 4, 2, 1, 3, 5, 6]))