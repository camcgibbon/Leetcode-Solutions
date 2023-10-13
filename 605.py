# Can Place Flowers

'''You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        if n == 0:
            return True
        if len(flowerbed) == 0:
            return False
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return True
            if flowerbed[0] == 1:
                return False
        else:
            for i in range(len(flowerbed)):
                if flowerbed[0] == 0 and flowerbed[1] == 0:
                    flowerbed[0] = 1
                    count += 1
                if i == len(flowerbed) - 1:
                    if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        count += 1
                if flowerbed[i-1] == 0 or flowerbed[i-1] == 1:
                    if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        count += 1
        if count >= n:
            return True
        else:
            return False