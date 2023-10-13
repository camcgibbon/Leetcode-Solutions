# Unique Number of Occurrences

'''Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.'''

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        nums = {}
        for num in arr:
            if num not in nums:
                nums[num] = 1
            else:
                nums[num] += 1
        seen = set()
        for key in nums:
            if nums[key] in seen:
                return False
            seen.add(nums[key])
        return True