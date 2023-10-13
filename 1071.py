# Greatest Common Divisor of Strings

'''For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(num1, num2):
            while num2 != 0:
                temp = num1
                num1 = num2
                num2 = temp % num2
            return num1
        l = list(str1)
        l2 = list(str2)
        final = []
        for i in range(min(len(l),len(l2))):
            if l[i] == l2[i]:
                final.append(l[i])
        gcd = gcd(len(l), len(l2))
        if len(final) != gcd:
            final = final[:gcd]
        for i in range(0,len(l),gcd):
            substring = l[i:i+gcd]
            if substring != final:
                return ''
        for i in range(0,len(l2),gcd):
            substring = l2[i:i+gcd]
            if substring != final:
                return ''
        return ''.join(final)