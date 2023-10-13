# Happy Number

'''Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.'''

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:    
            sum = 0
            for digit in str(n):
                dsq = int(digit)**2
                sum += dsq
            if sum in seen:
                return False
            seen.add(sum)
            n = sum
        return True