#You are given an m x n binary matrix grid. An island is a group of 1's
#(representing land) connected 4-directionally (horizontal or vertical.)
#You may assume all four edges of the grid are surrounded by water.

#The area of an island is the number of cells with a value 1 in the island.

#Return the maximum area of an island in grid. If there is no island,
#return 0.

#Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
#[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
#[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
#[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
#Output: 6
#Explanation: The answer is not 11, because the island must be
#connected 4-directionally.

class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        num = 1
        lst = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for row, col in lst:
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == 1:
                num += self.dfs(grid, row, col)
        return num
    
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area_islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area_islands = max(area_islands, self.dfs(grid, r, c))
        return area_islands
        
