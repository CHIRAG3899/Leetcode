#You are given an array of integers stones where stones[i] is the weight of the ith stone.
#We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
#If x == y, both stones are destroyed, and
#If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
#At the end of the game, there is at most one stone left.
#Return the smallest possible weight of the left stone. If there are no stones left, return 0.

#Example 1:

#Input: stones = [2,7,4,1,8,1]
#Output: 1
#Explanation: 
#We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
#we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
#we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
#we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
#Example 2:

#Input: stones = [1]
#Output: 1

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) != 1:
            stones.sort()
            if len(stones)>2:
                if stones[-1]==stones[-2]:
                    del stones[-1]
                    del stones[-1]
                elif stones[-1]>stones[-2]:
                    stones[-1]-=stones[-2]
                    del stones[-2]
            else:
                return stones[-1]-stones[-2]        
        return stones[0]


import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heapq is a Min-Heap implementation. Since we need max elements every time
        # I multiplied each element by -1
        stones = [-1 * stone for stone in stones]
        # Changed the stones array to a heap
        heapq.heapify(stones)
        # While we have >= 2 stones left
        while len(stones) > 1:
            # Getting top 2 elements and multiplying by -1 to get the original values
            firstStone = -1 * heapq.heappop(stones)
            secondStone = -1 * heapq.heappop(stones)
            # If both stones have same weight, both will get destroyed
            # Otherwise, smaller stone is destroyed and larger stone will have
            # weight large stone weight - small stone weight
            # Adding that weight to heap
            if firstStone != secondStone:
                heapq.heappush(stones, -1 * abs(firstStone - secondStone))
        # stones will be empty if last 2 stones we get have same weight
        # Otherwise we have 1 stone left
        return -1 * stones[0] if stones else 0