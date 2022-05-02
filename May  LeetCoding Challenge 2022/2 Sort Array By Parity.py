#Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
#
#Return any array that satisfies this condition.
#
# 
#
#Example 1:
#
#Input: nums = [3,1,2,4]
#Output: [2,4,3,1]
#Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
#Example 2:
#
#Input: nums = [0]
#Output: [0]

class Solution(object):
    def sortArrayByParity(self, A):
        A.sort(key = lambda x: x % 2)
        return A
        
class Solution:
    def sortArrayByParity(self, A):
        beg, end = 0, len(A) - 1
        
        while beg <= end:
            if A[beg] % 2 == 0:
                beg += 1
            else:
                A[beg], A[end] = A[end], A[beg]
                end -= 1
        return A