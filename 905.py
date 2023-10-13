# Sort Array By Parity

'''Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.'''

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        final = []
        for value in nums:
            if value % 2 == 0:
                final.append(value)
        for num in nums:
            if num % 2 != 0:
                final.append(num)
        return final