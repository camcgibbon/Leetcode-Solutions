# Reverse Vowels of a String

'''Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['A','a','E','e','I','i','O','o','U','u'])
        v = []
        for value in s:
            if value in vowels:
                v.append(value)
        v.reverse()
        new_string = ''
        for char in s:
            if char in vowels:
                char = v[0]
                v.pop(0)
            new_string = new_string + char
        return new_string