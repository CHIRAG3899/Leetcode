#Given a rectangular cake with height h and width w, and two arrays of
#integers horizontalCuts and verticalCuts where horizontalCuts[i] is the
#distance from the top of the rectangular cake to the ith horizontal cut and
#similarly, verticalCuts[j] is the distance from the left of the rectangular
#cake to the jth vertical cut.
#Return the maximum area of a piece of cake after you cut at each horizontal
#and vertical position provided in the arrays horizontalCuts and verticalCuts.
#Since the answer can be a huge number, return this modulo 10^9 + 7.

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts=sorted(horizontalCuts)
        verticalCuts=sorted(verticalCuts)        
        horizontalCuts.append(h)
        verticalCuts.append(w)
        horizontalCuts=[0]+horizontalCuts
        verticalCuts=[0]+verticalCuts
        max_height=0
        max_width=0
        for i in range(1,len(horizontalCuts)):
            max_height=max(horizontalCuts[i]-horizontalCuts[i-1],max_height)
            
        for i in range(1,len(verticalCuts)):
            max_width=max(verticalCuts[i]-verticalCuts[i-1],max_width)
            
        return max_height*max_width%1000000007
