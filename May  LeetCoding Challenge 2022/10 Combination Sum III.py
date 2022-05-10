#Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
#
#Only numbers 1 through 9 are used.
#Each number is used at most once.
#Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
#
# 
#
#Example 1:
#
#Input: k = 3, n = 7
#Output: [[1,2,4]]
#Explanation:
#1 + 2 + 4 = 7
#There are no other valid combinations.
#Example 2:
#
#Input: k = 3, n = 9
#Output: [[1,2,6],[1,3,5],[2,3,4]]
#Explanation:
#1 + 2 + 6 = 9
#1 + 3 + 5 = 9
#2 + 3 + 4 = 9
#There are no other valid combinations.
#Example 3:
#
#Input: k = 4, n = 1
#Output: []
#Explanation: There are no valid combinations.
#Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

class Solution(object):
    def combinationSum3(self, k, n):
        ret = []
        self.dfs(list(range(1, 10)), k, n, [], ret)
        return ret
    
    def dfs(self, nums, k, n, path, ret):
        if k < 0 or n < 0:
            return 
        if k == 0 and n == 0:
            ret.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k-1, n-nums[i], path+[nums[i]], ret)
            
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        a=[i for i in range(1,10)]
        ans=[]
        def dfs(s,c):
            if len(c)==k:
                if sum(c)==n:
                    ans.append(list(c))
                return
            elif len(c)>k:
                return
            for i in range(s,len(a)):
                c.append(a[i])
                dfs(i+1,c)
                c.pop()
        dfs(0,[])
        return ans
        
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
 
        for combination in range(1, 1<<10):
            C = []
            S = 0
            has_zero = False

            for digit in range(10):
                if combination & (1<<digit):
                    if digit == 0:
                        has_zero
                        break
                    
                    S += digit
                    if S > n:
                        break
                    
                    C.append(digit)
                    if len(C) > k:
                        break
                    
            if not has_zero and S == n and len(C) == k :
                ans.append(C)
        
        return ans