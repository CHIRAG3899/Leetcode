##Given an n x n matrix where each of the rows and columns is sorted in ascending order, return ##the kth smallest element in the matrix.

##Note that it is the kth smallest element in the sorted order, not the kth distinct element.

##You must find a solution with a memory complexity better than O(n2).

##Example 1:
##Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
##Output: 13
##Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest ##number is 13
##Example 2:
##Input: matrix = [[-5]], k = 1
##Output: -5

class Solution:
	def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

		result = []

		for row in matrix:

			result = result + row

		result = sorted(result)

		return result[k - 1]
		
class Solution:
	def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
            n, m = len(matrix), len(matrix[0])
            heap = [(matrix[0][j], 0, j) for j in range(m)]
            heapq.heapify(heap)
            while k > 0:
                result, i, j = heapq.heappop(heap)
                if i + 1 < n:
                    heapq.heappush(heap, (matrix[i+1][j], i + 1, j))
                k -= 1
            return result