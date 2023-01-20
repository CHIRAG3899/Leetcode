# Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

# Example 1:
# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

# Example 2:
# Input: nums = [4,4,3,2,1]
# Output: [[4,4]]

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ## RC ##
		## APPROACH : BACKTRACKING ##
        
		## TIME COMPLEXITY : O(N^2) ##
		## SPACE COMPLEXITY : O(N^2) ##
        
        def backtrack(curr, nums):
            if( len(curr) >= 2 and curr[-1] < curr[-2] ): return
            if( len(curr) >= 2 and curr[:] not in result):
                result.add(curr[:])
            for i in range(len(nums)):
                backtrack( curr + (nums[i],), nums[i+1:] )  # using tuples for curr instead of list
        result = set()
        backtrack( (), nums)
        return result
        
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        memo = defaultdict(int)
        n = len(nums)
        stack = [([nums[i]], i) for i in range(n - 1)]
        while stack:
            candidate, idx = stack.pop(0)
            if len(candidate) >= 2:
                res.append(candidate)
            for i in range(idx + 1, n):
                if nums[i] >= nums[idx]:
                    next_candidate = candidate + [nums[i]]
                    next_candidate_hashed = f'{next_candidate}'
                    if memo[next_candidate_hashed] == 0:
                        memo[next_candidate_hashed] = 1
                        stack.append((next_candidate, i))
        return res