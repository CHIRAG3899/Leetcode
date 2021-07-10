#Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.
#Example 1:
#Input: nums = [3,2,1]
#Output: 1
#Explanation: The third maximum is 1.
#Example 2:
#Input: nums = [1,2]
#Output: 2
#Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
#Example 3:
#Input: nums = [2,2,3,1]
#Output: 1
#Explanation: Note that the third maximum here means the third maximum distinct number.
#Both numbers with value 2 are both considered as second maximum.

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        max1 = nums[0]  #Initialised the max with first index
        secmax = float('-inf') 
        thirmax = float('-inf')
        #assuming second and third to be -infinity
        
        if len(nums)<3:
                return max(nums)
        #this won't run more than 2 times and hence we can consider this in our O(n) solution!
        # It isn't worth writing the Whole Loop logic here
        
        for i in range(len(nums)):
                num = nums[i]
                
				#Read the below if conditions to get the approach of updating First, second and third max respectively
				
                if (num>max1):
                        thirmax = secmax 
                        secmax = max1
                        max1 = nums[i]
                        
                elif(num>secmax and num<max1):
                        thirmax = secmax
                        secmax = num
                        
                elif(num>thirmax and num<secmax):
                        thirmax = num
                        
        return thirmax if thirmax != float('-inf') else max1
		#if condition when the elements get repeated such that thirdmax remains -infinity
