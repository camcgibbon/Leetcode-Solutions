# Max Consecutive Ones III

'''Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        max_value = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                k -= 1
            while k < 0:
                if nums[start] == 0:
                    k += 1
                start += 1
            max_value = max(max_value,end-start+1)
        return max_value