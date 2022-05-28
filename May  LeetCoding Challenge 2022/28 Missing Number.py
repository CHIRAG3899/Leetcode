#Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
#
# 
#
#Example 1:
#
#Input: nums = [3,0,1]
#Output: 2
#Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
#Example 2:
#
#Input: nums = [0,1]
#Output: 2
#Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
#Example 3:
#
#Input: nums = [9,6,4,2,3,5,7,0,1]
#Output: 8
#Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        list1 = list(range(0,len(nums) + 1))
        i = len(nums)
        while i > 0:
            if nums[0] == list1[0]:
                nums.pop(0)
                list1.pop(0)
            i -= 1

        return list1[0]
        
class Solution:
    def missingNumber(self, n: List[int]) -> int:
        n.append(-1)
        i, L = 0, len(n)
        while i != L:
        	if n[i] not in [i,-1]:
        		n[n[i]], n[i] = n[i], n[n[i]]
        	else:
        		if n[i] == -1: a = i
        		i += 1
        return a