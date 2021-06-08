'''
merge two sorted list.
could be null
'''
from linkedList import ListNode

def mergeTwoSortedLists(l1, l2):
    newHead = ListNode()
    cur = newHead
    n1, n2 = l1, l2
    while n1 or n2:
        v1 = n1.data if n1 else float('inf')
        v2 = n2.data if n2 else float('inf')
        if v1 < v2:
            cur.next = n1 
            n1 = n1.next
        else:
            cur.next = n2
            n2 = n2.next
        cur = cur.next
    return newHead.next
