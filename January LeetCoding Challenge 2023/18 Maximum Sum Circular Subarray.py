# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

# Example 1:
# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.

# Example 2:
# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

# Example 3:
# Input: nums = [-3,-2,-3]
# Output: -2
# Explanation: Subarray [-2] has maximum sum -2.

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
    
        # Method 1 : Kadane's Algorithm
        if max(A) <= 0:
            return max(A)
        
        max_sum = curr_max = min_sum = curr_min = A[0] 
        
        for i in range(1, len(A)): 
            curr_max = max(A[i], curr_max + A[i]) 
            max_sum = max(max_sum, curr_max)
            curr_min = min(A[i], curr_min + A[i]) 
            min_sum = min(min_sum, curr_min)
            
        return max(max_sum, sum(A) - min_sum)
            
        
        # Method 2 : Dynamic Programming
        if max(A) <= 0:
            return max(A)
            
        max_dp = [i for i in A]
        min_dp = [i for i in A]
        
        for i in range(1,len(A)):
            if max_dp[i-1] > 0:
                max_dp[i] += max_dp[i-1]
            if min_dp[i-1] < 0:
                min_dp[i] += min_dp[i-1]

        return max(max(max_dp), sum(A) - min(min_dp))
		
class Solution:
	def maxSubarraySumCircular(self, nums: List[int]) -> int:
		minS = (1 << 31)
		minSum = 0
		maxS = -(1 << 31)
		totSum = 0
		maxSum = 0
		for ele in nums:
			totSum += ele
			# Maximum Sum Subarray...
			maxSum += ele
			maxS = max(maxS, maxSum)
			if maxSum < 0:
				maxSum = 0
			# ...
			# Minimum Sum Subarray...
			minSum += ele
			minS = min(minS, minSum)
			if minSum > 0:
				minSum = 0
			# ...
		if(totSum == minS):
			return maxS
		return max(maxS, (totSum-minS))