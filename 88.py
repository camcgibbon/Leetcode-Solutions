# Merge Sorted Array

'''You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.'''

'''Merge nums1 and nums2 into a single array sorted in non-decreasing order.'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m-1, (m+n)-1):
            nums1.pop()
        for i in range(0, n):
            value = nums2[i]
            nums1.append(value)
        nums1.sort()