# Increasing Triplet Subsequence

'''Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.'''

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = float('inf')
        mid = float('inf')
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= mid:
                mid = num
            else:
                return True
        return False