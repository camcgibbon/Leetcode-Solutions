# Monotonic Array

'''An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.'''

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def isincreasing(n):
            prev = float('-inf')
            for num in n:
                if num >= prev:
                    prev = num
                    continue
                else:
                    return False
            return True
        def isdecreasing(n):
            prev = float('inf')
            for num in n:
                if num <= prev:
                    prev = num
                    continue
                else:
                    return False
            return True
        return isincreasing(nums) or isdecreasing(nums)