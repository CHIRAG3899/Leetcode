#We are given an array nums of positive integers, and two positive integers left
#and right (left <= right).
#Return the number of (contiguous, non-empty) subarrays such that the value of
#the maximum array element in that subarray is at least left and at most right.
#Example:
#Input: 
#nums = [2, 1, 4, 3]
#left = 2
#right = 3
#Output: 3
#Explanation: There are three subarrays that meet the requirements: [2], [2, 1],[3].

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans, low, mid = 0, 0, 0
        for num in nums:
            if num > right: mid = 0
            else:
                mid += 1
                ans += mid
            if num >= left: low = 0
            else:
                low += 1
                ans -= low
        return ans 
