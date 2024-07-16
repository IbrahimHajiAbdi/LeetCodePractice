from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def hasCycle(head: Optional[ListNode]) -> bool:
    if head is None:
        return False
    slow, fast = head, head.next
    while slow and fast:
        slow = slow.next
        fast = fast.next
        if fast:
            fast = fast.next
        else:
            return False
        if fast == slow:
            return True
    return False

print(hasCycle(ListNode(val=0, next=None)))