# String Compression

'''Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.'''

class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        while read < len(chars):
            count = 0
            char = chars[read]
            while read < len(chars) and chars[read] == char:
                count += 1
                read += 1
            chars[write] = char
            write += 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        chars = chars[:write]
        return len(chars)