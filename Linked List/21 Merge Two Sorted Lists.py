from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return f"ListNode({self.val}, {self.next})"

# def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#     res = ListNode()
#     while list1 is not None and list2 is not None:
#         if list1.val < list2.val:
#             res.next = ListNode(val=list1.val) 
#             list1 = list1.next
#             res = res.next
#         else:
#             res.next = ListNode(val=list2.val) 
#             list2 = list2.next
#             res = res.next

#     return res    
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = node = ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next
        node = node.next

    node.next = list1 or list2

    return dummy.next

print(mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))))