#Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
#
#Return true if there is a 132 pattern in nums, otherwise, return false.
#
# 
#
#Example 1:
#
#Input: nums = [1,2,3,4]
#Output: false
#Explanation: There is no 132 pattern in the sequence.
#Example 2:
#
#Input: nums = [3,1,4,2]
#Output: true
#Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
#Example 3:
#
#Input: nums = [-1,3,2,0]
#Output: true
#Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

class Solution:
    def find132pattern(self, nums):
        min_list = list(accumulate(nums, min))
        stack, n = [], len(nums)
        
        for j in range(n-1, -1, -1):
            if nums[j] > min_list[j]:
                while stack and stack[-1] <= min_list[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])           
        return False
        
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
      
        second_num = -math.inf
        stck = []
        # Try to find nums[i] < second_num < stck[-1]
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < second_num:
                return True
            # always ensure stack can be popped in increasing order
            while stck and stck[-1] < nums[i]:
				second_num = stck.pop()  # this will ensure  second_num < stck[-1] for next iteration

            stck.append(nums[i])
        return False