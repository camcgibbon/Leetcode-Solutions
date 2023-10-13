# Find the Difference of Two Arrays

'''Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.'''

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1s = set(nums1)
        nums2s = set(nums2)
        arr = [[],[]]
        for num in nums1s:
            if num not in nums2s:
                arr[0].append(num)
        for n in nums2s:
            if n not in nums1s:
                arr[1].append(n)
        return arr
