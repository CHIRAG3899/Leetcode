#You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
#Return true if you can make this square and false otherwise.
#Example 1:
#Input: matchsticks = [1,1,2,2,2]
#Output: true
#Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
#Example 2:
#Input: matchsticks = [3,3,3,3,4]
#Output: false
#Explanation: You cannot find a way to form a square with all the matchsticks.

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        N=len(matchsticks)
        perimeter=sum(matchsticks)
        sperimeter=perimeter//4
        
        if perimeter %4!=0:
            return False
        
        if any(x>sperimeter for x in matchsticks):
            return False
        has_cache=[[False]*(1<<N) for _ in range(4)]
        cache=[[False] *(1<<N) for _ in range(4)]
        def canMake(sides,usedMask):
            if sides==4:
                return True
            if has_cache[sides][usedMask]:
                return cache[sides][usedMask]
            has_cache[sides][usedMask]=True
            currentSide=sum(x for index,x in enumerate(matchsticks) if (usedMask & ( 1<<index)) >0) %sperimeter
            for index in range(N):
                if (usedMask &(1<<index)) ==0 and currentSide + matchsticks[index] <= sperimeter:
                    if currentSide+matchsticks[index]==sperimeter:
                        if canMake(sides+1,usedMask | (1<<index)):
                            cache[sides][usedMask]=True
                            return True
                    else:
                        if canMake(sides,usedMask |(1<<index)):
                            cache[sides][usedMask]=True
                            return True
            cache[sides][usedMask]=False
            return False
        return canMake(0,0)
