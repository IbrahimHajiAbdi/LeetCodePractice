# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return f"ListNode({self.val}, {self.next})"

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    num1 = 0
    multi = 1
    while l1:
        num1 += l1.val * multi
        multi *= 10
        l1 = l1.next
    num2 = 0
    multi = 1
    while l2:
        num2 += l2.val * multi
        multi *= 10
        l2 = l2.next
    total = num1 + num2
    print(total, num1, num2)
    res = ListNode()
    ptr = res
    for i in range(len(str(total))):
        ptr.next = ListNode(str(total)[len(str(total)) - i - 1])
        ptr = ptr.next 
    return res.next

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
print(addTwoNumbers(l1, l2))
