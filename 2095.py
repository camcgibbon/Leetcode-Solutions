# Delete the Middle Node of a Linked List

'''You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            if curr.val != None:
                length += 1
            curr = curr.next

        if length == 1:
            del head
            return
        if length == 0:
            return head

        mid = floor(length / 2)
        current = head
        for i in range(mid):
            if i == mid - 1:
                to_delete = current.next
                new_next = to_delete.next
                del to_delete
                current.next = new_next
                break
            current = current.next
        
        return head