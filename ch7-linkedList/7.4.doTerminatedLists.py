from linkedList import ListNode
import typing
def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    '''
    approach1 -> store everything in l0 in ht, iter thru l1 and see if any nodes are common
    O(m + n) time and O(m) space

    approach2 -> 
    O(m + n) time and O(1) space
    '''
    def getLength(l):
        length = 0
        cur = l
        while cur:
            length += 1
            cur = cur.next
        return length

    it0 = l0
    it1 = l1
    len0 = getLength(l0)
    len1 = getLength(l1)
    if len0 < len1:
        for _ in range(len1 - len0):
            it1 = it1.next
    else:
        for _ in range(len0 - len1):
            it0 = it0.next

    while it0:
        if it0 is it1:
            return it0
        it0 = it0.next
        it1 = it1.next
    
    return None
