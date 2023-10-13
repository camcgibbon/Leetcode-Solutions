# Asteroid Collision

'''We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i,num in enumerate(asteroids):
            if i == 0:
                stack.append(num)
                continue
            if stack != []:
                if num < 0 and stack[-1] > 0:
                    while abs(num) > abs(stack[-1]) and num < 0 and stack[-1] > 0:
                        stack.pop(-1)
                        if stack == []:
                            break
                    if stack == []:
                        stack.append(num)
                        continue
                    if abs(num) < abs(stack[-1]) and num < 0 and stack[-1] > 0:
                        continue
                    if abs(num) == abs(stack[-1]) and num < 0 and stack[-1] > 0:
                        stack.pop(-1)
                        continue
            stack.append(num)
        return stack