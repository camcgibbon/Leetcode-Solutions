# Determine if Two Strings Are Close

'''Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.'''

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        word1d = {}
        word2d = {}
        for char in word1:
            if char in word1d:
                word1d[char] += 1
            else:
                word1d[char] = 1
        for char in word2:
            if char in word2d:
                word2d[char] += 1
            else:
                word2d[char] = 1
        for key in word1d:
            if key not in word2d:
                return False
        arr = []
        arr2 = []
        for key in word1d:
            arr.append(word1d[key])
        for key in word2d:
            arr2.append(word2d[key])
        arr.sort()
        arr2.sort()
        if arr == arr2:
            return True
        return False