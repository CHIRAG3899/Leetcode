#On an N x N grid, each square grid[i][j] represents the elevation at that point
#(i,j).
#Now rain starts to fall. At time t, the depth of the water everywhere is t.
#You can swim from a square to another 4-directionally adjacent square if and
#only if the elevation of both squares individually are at most t. You can swim
#infinite distance in zero time. Of course, you must stay within the boundaries
#of the grid during your swim.
#You start at the top left square (0, 0). What is the least time until you can
#reach the bottom right square (N-1, N-1)?
#Example 1:
#Input: [[0,2],[1,3]]
#Output: 3
#Explanation:
#At time 0, you are in grid location (0, 0).
#You cannot go anywhere else because 4-directionally adjacent neighbors have a
#higher elevation than t = 0.
#You cannot reach point (1, 1) until time 3.
#When the depth of water is 3, we can swim anywhere inside the grid.
#Example 2:
#Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
#Output: 16
#Explanation:
# 0  1  2  3  4
#24 23 22 21  5
#12 13 14 15 16
#11 17 18 19 20
#10  9  8  7  6
#The final route is marked in bold.
#We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:            
        def canReach(t):
            nonlocal grid
            
            visited = [[False]*n for _ in range(n)]
            q = [(0,0)]
            
            while q:
                x, y = q.pop()
                visited[x][y]=True
                if x == m-1 and y==n-1:
                    return True
                
                for i,j in ((0,1),(1,0),(0,-1),(-1,0)):
                    if 0<=x+i<m and 0<=y+j<n and grid[x+i][y+j]<=t and grid[x][y]<=t and not visited[x+i][y+j]:
                        q.append((x+i,y+j))
                
            return False
            
        m, n = len(grid), len(grid[0]) 
        
        right = max(grid[i][j] for i in range(m) for j in range(n))
        left = 0
        
        while left<=right:
            mid = (left+right)//2
            if canReach(mid):
                right = mid-1
            else:
                left = mid+1
                
        return left
