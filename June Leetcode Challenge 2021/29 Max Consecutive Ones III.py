#Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
#Example 1:
#Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
#Output: 6
#Explanation: [1,1,1,0,0,1,1,1,1,1,1]
#Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
#Example 2:
#Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
#Output: 10
#Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
#Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

class Solution:
    def longestOnes(self, nums, k):
        beg, end, zeroes, ans = 0, 0, 0, 0
        while end < len(nums):
            if zeroes + (nums[end] == 0) <= k:
                zeroes += nums[end] == 0
                end += 1
                ans = max(ans, end - beg)
            else:
                zeroes -= nums[beg] == 0
                beg += 1  
        return ans
        
