#You are given an array of binary strings strs and two integers m and n.
#
#Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
#
#A set x is a subset of a set y if all elements of x are also elements of y.
##
## 
##
##Example 1:
##
##Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
##Output: 4
##Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
##Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
##{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
##Example 2:
##
##Input: strs = ["10","0","1"], m = 1, n = 1
##Output: 2
##Explanation: The largest subset is {"0", "1"}, so the answer is 2.

class Solution(object):
    def findMaxForm(self, strs, m, n):
        items = [[0,0] for i in range(len(strs))]
        for i in range(len(strs)):
            items[i][0] = strs[i].count('0')
            items[i][1] = strs[i].count('1')
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for item in items:
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i>=item[0] and j>=item[1]:
                        dp[i][j] = max(dp[i][j], dp[i-item[0]][j-item[1]]+1)
        return dp[-1][-1]
        
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        t=len(strs)
        @lru_cache(None)
        def dp(i,m,n):
            if i==t:
                return 0
            ans=0
            #dont take curr element
            ans+=dp(i+1,m,n)
            #take curr element
            L=[i for i in strs[i]]
            a,b=L.count('0'),L.count('1')
            ans=max(ans,(1+dp(i+1,m-a,n-b)) if m-a>=0 and n-b>=0 else 0)
            return ans
        return dp(0,m,n)
        
class Solution:
    def findMaxForm(self, strs, m, n):
        xy = [[s.count("0"), s.count("1")] for s in strs]

        @lru_cache(None)
        
        def dp(mm, nn, kk):
            if mm < 0 or nn < 0: return -float("inf")
            if kk == len(strs): return 0
            x, y = xy[kk]
            return max(1 + dp(mm-x, nn-y, kk + 1), dp(mm, nn, kk + 1))
        
        return dp(m, n, 0)