#Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.
#
#Write an algorithm to minimize the largest sum among these m subarrays.
#Example 1:
#
#Input: nums = [7,2,5,10,8], m = 2
#Output: 18
#Explanation:
#There are four ways to split nums into two subarrays.
#The best way is to split it into [7,2,5] and [10,8],
#where the largest sum among the two subarrays is only 18.
#Example 2:
#
#Input: nums = [1,2,3,4,5], m = 2
#Output: 9
#Example 3:
#
#Input: nums = [1,4,4], m = 3
#Output: 4

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        memo = [[0] * (m + 1) for _ in range(n)]
        
        # Create a prefix sum array of nums.
        prefix_sum = [0] + list(itertools.accumulate(nums))
        
        for subarray_count in range(1, m + 1):
            for curr_index in range(n):
                # Base Case: If there is only one subarray left, then all of the remaining numbers
                # must go in the current subarray. So return the sum of the remaining numbers.
                if subarray_count == 1:
                    memo[curr_index][subarray_count] = prefix_sum[n] - prefix_sum[curr_index]
                    continue

                # Otherwise, use the recurrence relation to determine the minimum largest subarray sum
                # between curr_index and the end of the array with subarray_count subarrays remaining.
                minimum_largest_split_sum = prefix_sum[n]
                for i in range(curr_index, n - subarray_count + 1):
                    # Store the sum of the first subarray.
                    first_split_sum = prefix_sum[i + 1] - prefix_sum[curr_index]

                    # Find the maximum subarray sum for the current first split.
                    largest_split_sum = max(first_split_sum, memo[i + 1][subarray_count - 1])

                    # Find the minimum among all possible combinations.
                    minimum_largest_split_sum = min(minimum_largest_split_sum, largest_split_sum)

                    if first_split_sum >= minimum_largest_split_sum:
                        break
            
                memo[curr_index][subarray_count] = minimum_largest_split_sum
        
        return memo[0][m]
        
class Solution:
    def splitArray(self, nums, m):
        n = len(nums)
        acc = [0] + list(accumulate(nums))
        dp = list(acc)
        
        for j in range(1, m):
            for i in range(n, j, -1):
                beg, end = j - 1, i
                while beg + 1 < end:
                    mid = (beg + end)//2
                    if dp[mid] >= acc[i] - acc[mid]:
                        end = mid
                    else:
                        beg = mid
                    dp[i] = min(max(dp[end], acc[i] - acc[end]), max(dp[beg], acc[i] - acc[beg]))
        
        return dp[-1]

class Solution:
    def splitArray(self, nums, m):
        def check(Q):
            if max(nums) > Q: return False
            acc, ans = 0, 1
            for num in nums:
                if acc + num <= Q:
                    acc += num
                else:
                    acc = num
                    ans += 1
            return ans <= m
        
        beg, end = max(nums) - 1, sum(nums)
        while beg + 1 < end:
            mid = (beg + end)//2
            if check(mid):
                end = mid
            else:
                beg = mid
        
        return end