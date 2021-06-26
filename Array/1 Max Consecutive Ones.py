#Given a binary array nums, return the maximum number of consecutive 1's in the
#array.
#Example 1:
#Input: nums = [1,1,0,1,1,1]
#Output: 3
#Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
#Example 2:
#Input: nums = [1,0,1,1,0,1]
#Output: 2

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1s, counter = 0, 0
        for n in nums:
            if n == 1:
                counter += 1
            else:
                max1s = max(max1s, counter)
                counter = 0
        return max(max1s, counter)
