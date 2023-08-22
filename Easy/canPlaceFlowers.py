class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        #iterate through list flowerbed
        #count sequences of 0 and see how many flowers can fit per sequence 
        
        flowerCount = 0
        for i in range(len(flowerbed)):
            print("i:", i, "flower:", flowerbed[i])
            if i == 0 and len(flowerbed) != 1 and flowerbed[i] == 0 and flowerbed[i+1] != 1:
                flowerCount += 1
                flowerbed[i] = 1
            elif flowerbed[i] == 1:
                flowerCount += 0
            elif i != len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                flowerCount += 1
                flowerbed[i] = 1
                print("flowerbed new:", flowerbed[i])
            elif i == len(flowerbed) - 1 and flowerbed[i-1] == 0:
                flowerCount += 1
                flowerbed[i] = 1
            elif flowerbed[i] == 0 and flowerbed[i-1] == 1:
                flowerCount += 0
            
        print("flowercount:", flowerCount)
        if n <= flowerCount:
            return True
        else:
            return False
