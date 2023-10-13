# Longest Subarray of 1's After Deleting One Element

'''Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.'''

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        zeros = 0
        max_value = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                zeros += 1
            while start < len(nums) and zeros > 1:
                if nums[start] == 0:
                    zeros -= 1
                start += 1
            max_value = max(max_value,end-start)
        return max_value