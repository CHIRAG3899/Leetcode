#You are given a 0-indexed integer array nums and an integer k.
#You are initially standing at index 0. In one move, you can jump at most
#k steps forward without going outside the boundaries of the array. That is,
#you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.
#You want to reach the last index of the array (index n - 1). Your score is
#the sum of all nums[j] for each index j you visited in the array.
#Return the maximum score you can get.
#Example 1:
#Input: nums = [1,-1,-2,4,-7,3], k = 2
#Output: 7
#Explanation: You can choose your jumps forming the subsequence [1,-1,4,3]
#(underlined above). The sum is 7.
#Example 2:
#Input: nums = [10,-5,-2,4,0,3], k = 3
#Output: 17
#Explanation: You can choose your jumps forming the subsequence [10,4,3]
#(underlined above). The sum is 17.

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n=len(nums)
        dp=[-sys.maxsize]*n
        dp[0]=nums[0]
        dec_q=deque([0])
        
        k+=1
        for i in range(1,n):
            if i>=k and dec_q[0]==i-k:
                dec_q.popleft()
            
            dp[i]= nums[i]+dp[dec_q[0]]
            
            while dec_q and dp[dec_q[-1]] <= dp[i]:
                dec_q.pop()
            
            dec_q.append(i)
            
        return dp[-1]
