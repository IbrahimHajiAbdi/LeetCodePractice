from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return f"ListNode({self.val}, {self.next})"

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    def helper(node):
        if node.next != None:        
            return helper(node.next)
        return ListNode(val=node.val)
            
list = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))))
reverseList(list)