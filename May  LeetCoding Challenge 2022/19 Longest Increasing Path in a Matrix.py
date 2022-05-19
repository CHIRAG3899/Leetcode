#Given an m x n integers matrix, return the length of the longest increasing path in matrix.
#
#From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
#
# 
#
#Example 1:
#
#
#Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
#Output: 4
#Explanation: The longest increasing path is [1, 2, 6, 9].
#Example 2:
#
#
#Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
#Output: 4
#Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
#Example 3:
#
#Input: matrix = [[1]]
#Output: 1

class Solution:
    def longestIncreasingPath(self, matrix):
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
            return dp[i][j]

        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for i in range(M)]
        return max(dfs(x, y) for x in range(M) for y in range(N))
        
class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        directions = [0, 1, 0, -1, 0] # four directions 
        
        @lru_cache(maxsize=None) # using python cache lib for memoization
        def dfs(r,c):
            ans=1                  
			# iterating through all 4 directions
            for i in range(4): 
                new_row,new_col=r+directions[i], c+directions[i+1] # calculating the new cell
				# check if new cell is within the grid bounds and is an increasing sequence
                if 0<=new_row<m and 0<=new_col<n and grid[new_row][new_col]>grid[r][c]: 
                    ans = max(ans, dfs(new_row, new_col) + 1 )  # finding the max length of valid path from the current cell                                      
            return ans
        
        return max(dfs(r,c) for r in range(m) for c in range(n)) 