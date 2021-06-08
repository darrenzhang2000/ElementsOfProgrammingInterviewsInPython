def has_cycle(head):
    slow, fast = head, head.next
    while fast != None:
        if fast is slow: # cycle found 
            break
        slow = slow.next
        fast = fast.next.next if fast.next else None

    if fast == None:
        return None

    # find cycle length
    cycleLength = 0
    while True:
        slow = slow.next
        fast = fast.next.next
        cycleLength += 1
        if slow is fast:
            break
    print('q')
    cycleIt = head
    for _ in range(cycleLength):
        cycleIt = cycleIt.next 
    # d = p + c. now cycle it is p steps behind the start of cycle, where p is distance from head to start of cycle

    startIt = head
    while not startIt is cycleIt:
        startIt = startIt.next
        cycleIt = cycleIt.next
    return startIt


