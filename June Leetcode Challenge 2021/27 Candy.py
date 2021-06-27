#There are n children standing in a line. Each child is assigned a rating value
#given in the integer array ratings.
#You are giving candies to these children subjected to the following requirements:
#Each child must have at least one candy.
#Children with a higher rating get more candies than their neighbors.
#Return the minimum number of candies you need to have to distribute the candies to the children.
#Example 1:
#Input: ratings = [1,0,2]
#Output: 5
#Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
#Example 2:
#Input: ratings = [1,2,2]
#Output: 4
#Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
#The third child gets 1 candy because it satisfies the above two conditions.

import heapq
class Solution:
    def candy(self, ratings):
        res = [1]*len(ratings)
        q = []
        for i in range(len(ratings)):
            heapq.heappush(q,[ratings[i],i])
        while(len(q)>0):
            rating,x = heapq.heappop(q)
            if x-1>=0:
                if ratings[x-1]<ratings[x]:
                    res[x] = max(res[x],res[x-1]+1)
            if x+1<len(res):
                if ratings[x+1]<ratings[x]:
                    res[x] = max(res[x],res[x+1]+1)
        return sum(res)
