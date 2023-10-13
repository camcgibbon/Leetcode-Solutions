# Add Two Numbers

'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_over = 0
        l3 = ListNode()
        head = l3
        while l1 and l2:
            total = l1.val + l2.val + carry_over
            carry_over = 0
            if total >= 10:
                total = total % 10
                carry_over = 1
            l3.val = total
            l1 = l1.next
            l2 = l2.next
            if l1 and l2:
                dummy = ListNode()
                l3.next = dummy
                l3 = dummy
        if l1:
            l3.next = l1
            if carry_over == 1:
                while l1:
                    total = l1.val + carry_over
                    carry_over = 0
                    if total >= 10:
                        total = total % 10
                        carry_over = 1
                    l1.val = total
                    l1 = l1.next
                    l3 = l3.next
        if l2:
            l3.next = l2
            if carry_over == 1:
                while l2:
                    total = l2.val + carry_over
                    carry_over = 0
                    if total >= 10:
                        total = total % 10
                        carry_over = 1
                    l2.val = total
                    l2 = l2.next
                    l3 = l3.next
        if carry_over:
            l3.next = ListNode(1)
        return head