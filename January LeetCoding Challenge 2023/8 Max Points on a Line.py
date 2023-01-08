# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

# Example 1:

# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
# Example 2:

# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # check for edge case
        if len(points)<3:
            return len(points)
        
        maxlen = 0
        for i in range(len(points)):
            line = {}
            for j in range(i+1,len(points)):
                y = points[i][1] - points[j][1]
                x = points[i][0] - points[j][0]
                
                # for finding the y-intercept (b)
                # b = points[i][0] if x == 0  else points[i][1] - ((y/x) * points[i][0])
                
                # use the slop as the hash map key
                slop = y/x if x!=0 else inf
                
                if slop in line:
                    line[slop]+= 1
                else:
                    line[slop] = 2 
                maxlen = max(line[slop] , maxlen)
        return maxlen
        
