# Container With Most Water

'''You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        def area(l,r):
            return min(height[l],height[r]) * (r - l)
        
        m = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if m < area(left,right):
                m = area(left,right)
            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                left += 1

        return m