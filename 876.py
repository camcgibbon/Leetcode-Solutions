# Middle of the Linked List

'''Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            if curr.val != None:
                length += 1
            curr = curr.next
        middle = floor(length / 2)
        for i in range(middle):
            head = head.next
        return head