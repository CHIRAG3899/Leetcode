#Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
#More formally check if there exists two indices i and j such that :
#i != j
#0 <= i, j < arr.length
#arr[i] == 2 * arr[j]
#Example 1:
#Input: arr = [10,2,5,3]
#Output: true
#Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
#Example 2:
#Input: arr = [7,1,14,11]
#Output: true
#Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.
#Example 3:
#Input: arr = [3,1,7,11]
#Output: false
#Explanation: In this case does not exist N and M, such that N = 2 * M.

class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        zero_count = 0 # To count the zeros
        for num in arr:
            if num != 0 and num * 2 in arr: #  check for mulipication by 2 
                return True
            elif num == 0 :
                zero_count += 1
        
        return True if zero_count > 1 else False
