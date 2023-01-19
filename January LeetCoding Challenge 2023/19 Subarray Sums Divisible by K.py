# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

# A subarray is a contiguous part of an array.

# Example 1:
# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

# Example 2:
# Input: nums = [5], k = 9
# Output: 0

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        prefix_sum = 0
        sums = {0: 1}
        answer = 0
        for num in A:
            prefix_sum += num
            key = prefix_sum%K
            if key in sums:
                answer += sums[key]
                sums[key] += 1
                continue
            sums[key] = 1
        return answer
        
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0 # Initialize variable to keep track of count
        sm = 0 # Initialize variable to keep track of running sum
        mod = 0 # Initialize variable to store remainder
        mp = {} # Initialize dictionary to keep track of the number of occurrences of each remainder
        mp[mod] = 1 # Initial remainder is 0
        for i in range(len(nums)):
            sm += nums[i] # Update running sum
            mod = sm % k # Update remainder
            if mod < 0:
                mod += k # If remainder is negative, add k to make it positive
            if mod in mp:
                count += mp[mod] # If remainder is already present in dictionary, add the number of occurrences of that remainder to the count
                mp[mod] += 1 # Increment the count for that remainder in the dictionary
            else:
                mp[mod] = 1 # If remainder is not present in the dictionary, add it with a count of 1
        return count