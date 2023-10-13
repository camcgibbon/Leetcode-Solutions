# Group Anagrams

'''Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        words = set()
        for word in strs:
            sorted_chars = sorted(list(word))
            sorted_word = ''.join(sorted_chars)
            if sorted_word not in words:
                words.add(sorted_word)
                d[sorted_word] = []
                d[sorted_word].append(word)
                continue
            for element in words:
                if element == sorted_word:
                    new = element
            d[new].append(word)
        final_list = []
        for value in d:
            final_list.append(d[value])
        return final_list