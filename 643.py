# Maximum Average Subarray I

'''You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.'''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = k - 1
        window_sum = sum(nums[start:end+1])
        averages = []
        averages.append(window_sum / k)
        while end < len(nums):
            window_sum = window_sum - nums[start]
            start += 1
            end += 1
            if end < len(nums):
                window_sum = window_sum + nums[end]
            averages.append(window_sum / k)
        return max(averages[0:len(averages)-1])