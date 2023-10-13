# Add Digits

'''Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.'''

class Solution:
    def addDigits(self, num: int) -> int:
        var = 0
        for n in str(num):
            if len(str(num)) == 1:
                return int(n)
            var += int(n)
        return self.addDigits(var)