#Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
#Integers in each row are sorted from left to right.
#The first integer of each row is greater than the last integer of the previous row.
# 
#Example 1:
#Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
#Output: true
#Example 2:
#Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
#Output: false

class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: return False
        m, n = len(matrix[0]), len(matrix)
        beg, end = 0, m*n - 1
        while beg < end:
            mid = (beg + end)//2
            if matrix[mid//m][mid%m] < target:
                beg = mid + 1
            else:
                end = mid
        return matrix[beg//m][beg%m] == target