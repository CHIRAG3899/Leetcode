# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

 

# Example 1:

# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
# - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
# Example 2:

# Input: points = [[1,2],[3,4],[5,6],[7,8]]
# Output: 4
# Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
# Example 3:

# Input: points = [[1,2],[2,3],[3,4],[4,5]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
# - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

class Solution:
    def findMinArrowShots(self, points):
        n = len(points)
        if n<2:
            return n

        #sort by start and end point
        START, END = 0,1
        points.sort(key=lambda i: (i[START],i[END]) )
        prev, cur = points[0], None
        darts = 0

        for i in range(1, n):
            cur = points[i]

            if cur[START] <= prev[END]:
                #overlap, wait for more overlap to throw dart
                prev = [cur[START], min(cur[END],prev[END])]
            else:
                #no overlap, throw dart at previous
                darts += 1
                prev = cur
		
		#pop the last balloon and return
        return darts+1

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points.sort(key = lambda a:a[1])
        arrows = 1
        curr = points[0]
        for balloon in points:
            if curr[1] < balloon[0]:
                curr = balloon
                arrows+=1
        return arrows
        
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        p = points[0][0]
        q = points[0][1]
        ans = 0
        for i,j in points:
            if p <= i <= q or p <= j <= q:
                p = max(i,p)
                q = min(j,q)
            else:
                ans += 1
                p = i
                q = j
        return ans + 1