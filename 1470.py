# Shuffle the Array

'''Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].'''

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        arr2 = []
        arr3 = []
        for i in range(n):
            arr.append(nums[i])
        for x in range(n, 2 * n):
            arr2.append(nums[x])
        for y in range(n):
            arr3.append(arr[y])
            arr3.append(arr2[y])
        return arr3