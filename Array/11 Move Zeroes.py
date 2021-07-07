#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#Note that you must do this in-place without making a copy of the array.
#Example 1:
#Input: nums = [0,1,0,3,12]
#Output: [1,3,12,0,0]
#Example 2:
#Input: nums = [0]
#Output: [0]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        index = 0
        
        for i in range(len(nums)):
            # If nums[i] != 0 then placing it in the "index" position of array
            if nums[i] != 0:
                nums[index] = nums[i]
                # Below line is used to optimize the solution. It makes the current i
                # position 0.
                # If this line is not used, we need to place all the remaining indices
                # to zero after this for loop is completed, by
                #   for i in range(index, len(nums)):
                #       nums[i] = 0
                if index != i: nums[i] = 0
                index += 1
