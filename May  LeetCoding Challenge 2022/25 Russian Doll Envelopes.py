#You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.
#
#One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.
#
#Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).
#
#Note: You cannot rotate an envelope.
#
# 
#
#Example 1:
#
#Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
#Output: 3
#Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
#Example 2:
#
#Input: envelopes = [[1,1],[1,1],[1,1]]
#Output: 1

class Solution:
    def maxEnvelopes(self, envelopes):
        nums = sorted(envelopes, key = lambda x: [x[0], -x[1]])    
        dp = [10**10] * (len(nums) + 1)
        for elem in nums: dp[bisect_left(dp, elem[1])] = elem[1]  
        return dp.index(10**10)
        
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key = lambda x: (x[0], -x[1]))
        stack = [0]
        for i in range(1, len(envelopes)):
            if envelopes[i][1] > envelopes[stack[-1]][1]:
                stack.append(i)
            else:
                left = self.binarySearch(envelopes, stack, i)
                stack[left] = i
        return len(stack)
    
    def binarySearch(self, envelopes, stack, curr):
        left, right = 0, len(stack)-1
        while left < right:
            mid = (left+right) // 2
            if envelopes[stack[mid]][1] == envelopes[curr][1]:
                return mid
            elif envelopes[stack[mid]][1] > envelopes[curr][1]:
                right = mid
            else:
                left = mid + 1
        return left
        
class Solution:
    def maxEnvelopes(self, e: List[List[int]]) -> int:
        e.sort(key=lambda f: (f[0], -f[1]))
        res = [e[0][1]]
        for i in range(1, len(e)):
            w, h = e[i][0],e[i][1]
            if w == e[i-1]:
                pass
            l = bisect_left(res, h)
            if l == len(res): res.append(h)
            else: res[l] = h
        return len(res)