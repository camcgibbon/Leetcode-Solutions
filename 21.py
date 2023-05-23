# Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sorted = []
        while list1:
            sorted.append(list1.val)
            list1 = list1.next
        while list2:
            sorted.append(list2.val)
            list2 = list2.next
        
        sorted.sort()

        dummy = ListNode()
        current = dummy
        for n in sorted:
            current.next = ListNode(n)
            current = current.next
        return dummy.next