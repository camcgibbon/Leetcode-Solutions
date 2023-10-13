# Maximum Number of Vowels in a Substring of Given Length

'''Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        start = 0
        end = k - 1
        totals = []
        max_vowels = 0
        for char in s[start:end+1]:
            if char in vowels:
                max_vowels += 1
        totals.append(max_vowels)
        while end < len(s):
            if s[start] in vowels:
                max_vowels -= 1
            start += 1
            end += 1
            if end < len(s) and s[end] in vowels:
                max_vowels += 1
            totals.append(max_vowels)
        return max(totals)