#Given an unsorted array of integers nums, return the length of the longest
#consecutive elements sequence.
#You must write an algorithm that runs in O(n) time.
#Example 1:
#Input: nums = [100,4,200,1,3,2]
#Output: 4
#Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
#Therefore its length is 4.
#Example 2:
#Input: nums = [0,3,7,2,5,8,4,6,0,1]
#Output: 9

class Solution(object):
   def longestConsecutive(self, a):
      a = set(a)
      longest = 0
      for i in a:
         if i-1 not in a:
            current = i
            streak = 0
            while i in a:
               i+=1
               streak+=1
               longest = max(longest,streak)
      return longest
