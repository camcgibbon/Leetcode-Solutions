# Odd Even Linked List

'''Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        dummy = curr.next
        while curr.next:
            next_node = curr.next
            if not curr.next.next:
                curr.next = dummy
                return head
            curr.next = curr.next.next
            next_node.next = next_node.next.next
            curr = curr.next
        curr.next = dummy
        return head