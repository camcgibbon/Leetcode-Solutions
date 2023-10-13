# Single Number

'''Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
                continue
            seen.add(num)
        for value in seen:
            return value