#Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
#
#Example 1:
#Input: n = 3
#Output: [[1,2,3],[8,9,4],[7,6,5]]
#
#Example 2:
#Input: n = 1
#Output: [[1]]

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None for j in range(n)] for i in range(n)]
        
        num = 1
        rowS, rowE, colS, colE = 0, n-1, 0, n-1
        
        # Walk in spriral form while inserting the number at each cell will give the result.
        while rowE >= 0 and colE >= 0:
            if rowS <= rowE:
                for col in range(colS, colE+1):
                    matrix[rowS][col] = num
                    num += 1
            rowS += 1
            
            if colS <= colE:
                for row in range(rowS, rowE+1):
                    matrix[row][colE] = num
                    num += 1
            colE -= 1
            
            if rowS <= rowE:
                for col in range(colE, colS-1, -1):
                    matrix[rowE][col] = num
                    num += 1
            rowE -= 1
            
            if colS <= colE:
                for row in range(rowE, rowS-1, -1):
                    matrix[row][colS] = num
                    num += 1
            colS += 1
        return matrix

def is_invalid(matrix, r, c, n):
    return r >= n or c >= n or r < 0 or c < 0 or matrix[r][c] != 0

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r = 0
        c = 0
        _dir = 0
        count = 1
        while count <= n * n:
            matrix[r][c] = count
            if is_invalid(matrix, r + direction[_dir][0], c + direction[_dir][1], n):
                _dir = (_dir + 1) % 4
            r += direction[_dir][0]
            c += direction[_dir][1]
            count += 1
        return matrix

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
       
        #Matrix we're going to return
        matrix = [[1] * n for _ in range(n)]
        
        #Initialize our boundaries
        top = -1
        bottom = n
        left = -1
        right = n
        
        #currVal will iterate up to n ^ 2
        currVal = 1
        
        #Current Row and Column we're in
        r, c = 0, 0
        
        #while the vertical and horizonal boundaries do not intersect
        while left < right and top < bottom:
            
            #Left to Right
            while c < right:
                matrix[r][c] = currVal
                c += 1
                currVal += 1
                
            #Correct position
            c -= 1
            top += 1
            r += 1
            
            #Top to Bottom
            while r < bottom:
                matrix[r][c] = currVal
                r += 1
                currVal += 1
            
            #Correct position
            r -= 1
            right -= 1
            c -= 1
            
            #Right to Left
            while c > left:
                matrix[r][c] = currVal
                c -= 1
                currVal += 1
            
            #Correct position
            c += 1
            bottom -= 1
            r -= 1
            
            #Bottom to Top
            while r > top:
                matrix[r][c] = currVal
                r -= 1
                currVal += 1
            
            #Correct position
            r += 1
            left += 1
            c += 1
            
        #Return our matrix, now with values filled in
        return matrix

