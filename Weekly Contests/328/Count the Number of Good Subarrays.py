# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A subarray arr is good if it there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [1,1,1,1,1], k = 10
# Output: 1
# Explanation: The only good subarray is the array nums itself.

# Example 2:
# Input: nums = [3,1,4,3,2,2,4], k = 2
# Output: 4
# Explanation: There are 4 different good subarrays:
# - [3,1,4,3,2,2] that has 2 pairs.
# - [3,1,4,3,2,2,4] that has 3 pairs.
# - [1,4,3,2,2,4] that has 2 pairs.
# - [4,3,2,2,4] that has 2 pairs.

class Solution:
    def countGood(self, nums, k):
        n = len(nums)
        freq = Counter() # Count occurance of number
        i,j = 0,0
        paircnt = 0
        ans = 0
        while i < n and j < n:
            freq[nums[j]] += 1
            if freq[nums[j]] > 1:
                paircnt += freq[nums[j]]-1
            while paircnt >= k and i <= j:
                ans += n-j
                if freq[nums[i]] > 1:
                    paircnt -= freq[nums[i]]-1
                freq[nums[i]] -= 1
                i += 1
            j += 1
                
        return ans
        
class Solution:
    def countGood(self, A: List[int], k: int) -> int:
        D = defaultdict(int)
        ans = cnt = l = 0
        for i in A:
            cnt += D[i]
            D[i] += 1
            while cnt >= k:
                D[A[l]] -= 1
                cnt -= D[A[l]]
                l += 1
            ans += l
        return ans