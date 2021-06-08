from list_node import ListNode

# Delete the node past this one. Assume node is not a tail.
def delete_after(node: ListNode) -> None:
    nextNode = node.next
    node.next = nextNode.next
    return