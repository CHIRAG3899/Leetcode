#According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
#
#The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
#
#Any live cell with fewer than two live neighbors dies as if caused by under-population.
#Any live cell with two or three live neighbors lives on to the next generation.
#Any live cell with more than three live neighbors dies, as if by over-population.
#Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
#The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
#
#Example 1:
#Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
#Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
#
#Example 2:
#Input: board = [[1,1],[1,0]]
#Output: [[1,1],[1,1]]

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i, j in product(range(m), range(n)):
            cnt = 0
            for di, dj in product(range(-1, 2), repeat=2):
                if di != 0 or dj != 0:
                    ii, jj = i + di, j + dj
                    if 0 <= ii < m and 0 <= jj < n:
                        cnt += board[ii][jj] & 1
            if cnt == 3 or (cnt == 2 and board[i][j] & 1): # Game-of-Life rule
                board[i][j] |= 2
        # print(board)
        for i, j in product(range(m), range(n)):
            board[i][j] >>= 1

def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def findNoofneighbours(row,col,board):
            top=dfs(row-1,col,board)
            bottom=dfs(row+1,col,board)
            left=dfs(row,col-1,board)
            right=dfs(row,col+1,board)
            topleft=dfs(row-1,col-1,board)
            topright=dfs(row-1,col+1,board)
            bottomleft=dfs(row+1,col-1,board)
            bottomright=dfs(row+1,col+1,board)
            return top+bottom+left+right+topright+bottomleft+bottomright+topleft
        def dfs(row,col,board2):
            if(row<len(board2) and col<len(board2[0]) and row>=0 and col>=0):
                return  board2[row][col]
            return 0
        board2=[]
        for i in board:
            board2.append(i.copy())
        for i in board2:
            print(i)
        for i in range(len(board2)):
            for j in range(len(board2[0])):
                neighbours=findNoofneighbours(i,j,board2)
                if(neighbours<2 and board2[i][j]==1):
                    board[i][j]=0
                elif((neighbours==2 or neighbours==3) and board2[i][j]==1):
                    board[i][j]=1
                elif(neighbours>3 and board2[i][j]==1):
                    board[i][j]=0
                elif(neighbours==3 and board2[i][j]==0):
                    board[i][j]=1
        return board

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                
                # count number of live neighbours
                live_neighbours = 0
                for x in range(max(i-1, 0), min(i+2, m)):
                    for y in range(max(j-1, 0), min(j+2, n)):
                        if i == x and j == y:
                            continue
                        live_neighbours += board[x][y] % 2
                
                # mark the cell if it needs to change states
                if board[i][j] == 0:
                    if live_neighbours == 3:
                        board[i][j] = 2
                elif live_neighbours < 2 or live_neighbours > 3:
                    board[i][j] = 3
        
        # change all required states
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0