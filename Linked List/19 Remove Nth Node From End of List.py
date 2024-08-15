from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"ListNode({self.val}, {self.next})"
    
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
    reversed = reverse(head)
    dummy = ListNode(0, reversed)
    curr, prev = reversed, None
    if n == 1:
        return reverse(reversed.next)
    for i in range(n, 0, -1):
        if i != 1:
            prev = curr
            curr = curr.next
        else:
            prev.next = curr.next
    return reverse(dummy.next)
        
    
l1 = ListNode(5, ListNode(6, ListNode(7)))
print(removeNthFromEnd(l1, 2))