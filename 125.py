# Valid Palindrome

'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.'''

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = re.sub(r'[\W_]+', '', s)
        string = string.lower()
        left, right = 0, len(string) - 1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True