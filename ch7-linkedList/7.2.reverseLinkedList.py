from linkedList import ListNode


def reverse_sublist(L, start,
                    finish):
    if start == finish:
        return L
    beforeNode = getNthNode(L, start - 1) if start != 1 else None
    oldHead = beforeNode.next if beforeNode else L
    oldTail = getNthNode(L, finish)
    afterNode = oldTail.next
    newHead, newTail = reverseLinkedList(oldHead, oldTail)
    # reattach nodes
    if beforeNode:
        beforeNode.next = newHead
    newTail.next = afterNode # afterNode could be null
    return L if start != 1 else newHead

def reverseLinkedList(head, tail):
    newHead = tail
    newTail = head
    prev = head
    cur = head.next
    while True:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
        if prev == tail:
            break
    return newHead, newTail
        
def getNthNode(L, n):
    cur = L
    for _ in range(1, n):
        if not cur:
            return None
        cur = cur.next
    return cur

head = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
# l4 = ListNode(4)
head.next = l2
l2.next = l3
# l3.next = l4

def printLinkedList(n):
    cur = n
    while cur:
        print(cur.data)
        cur = cur.next
printLinkedList(reverse_sublist(head, 2, 3))



# def reverse_sublist(L, start,
#                     finish):
#     if start == finish:
#         return L
    
#     head = L
#     for _ in range(1, start):
#         head = head.next
#     beforeHead = L if head == L else None
#     while beforeHead and beforeHead.next != head:
#         beforeHead = beforeHead.next

#     tail = L
#     for _ in range(1, finish):
#         tail = tail.next
#     afterTail = tail.next
#     print('z', tail.data)


#     reverseLinkedList(beforeHead, head, tail, afterTail)
#     print('z', head.data, tail.data)
#     return L if start != 1 else tail

# def reverseLinkedList(beforeHead, head, tail, afterTail):
#     prev = head
#     cur = head.next
#     while cur != tail:
#         temp = cur.next
#         cur.next = prev
#         prev = cur 
#         cur = temp
#     cur.next = prev
#     if beforeHead:
#         beforeHead.next = tail
#     head.next = afterTail
    

