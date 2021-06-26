#You are given an integer array nums and you have to return a new counts
#array. The counts array has the property where counts[i] is the number of
#smaller elements to the right of nums[i].
#Example 1:
#Input: nums = [5,2,6,1]
#Output: [2,1,1,0]
#Explanation:
#To the right of 5 there are 2 smaller elements (2 and 1).
#To the right of 2 there is only 1 smaller element (1).
#To the right of 6 there is 1 smaller element (1).
#To the right of 1 there is 0 smaller element.
#Example 2:
#Input: nums = [-1]
#Output: [0]
#Example 3:
#Input: nums = [-1,-1]
#Output: [0,0]

from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        sortedList = SortedList()
        for i in range(n - 1, -1, -1):
            index = sortedList.bisect_left(nums[i])
            ans[i] = index
            sortedList.add(nums[i])
        return ans
