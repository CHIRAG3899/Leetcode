#Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.
#It is guaranteed that there will be a rectangle with a sum no larger than k.
#Example 1:
#Input: matrix = [[1,0,1],[0,-2,3]], k = 2
#Output: 2
#Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).
#Example 2:
#Input: matrix = [[2,2,-1]], k = 3
#Output: 3

from sortedcontainers import SortedList
    
class Solution:
    def maxSumSubmatrix(self, M, k):
        def countRangeSum(nums, U):
            SList, ans = SortedList([0]), -float("inf")
            for s in accumulate(nums):
                idx = SList.bisect_left(s - U) 
                if idx < len(SList): ans = max(ans, s - SList[idx])        
                SList.add(s)
            return ans
        
        m, n, ans = len(M), len(M[0]), -float("inf")
        
        for i, j in product(range(1, m), range(n)):
            M[i][j] += M[i-1][j]
                
        M = [[0]*n] + M
        
        for r1, r2 in combinations(range(m + 1), 2):
            row = [j - i for i, j in zip(M[r1], M[r2])]
            ans = max(ans, countRangeSum(row, k))
            
        return ans
