# Contains Duplicate

'''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        for num in nums:
            if num in myset:
                return True
            myset.add(num)
        return False