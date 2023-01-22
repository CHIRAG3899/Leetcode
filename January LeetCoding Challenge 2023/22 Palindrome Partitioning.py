# Given a string s, partition s such that every 
# substring
 # of the partition is a 
# palindrome
# . Return all possible palindrome partitioning of s.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"
# Output: [["a"]]

class Solution(object):
    @cache  # the memory trick can save some time
    def partition(self, s):
        if not s: return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  # prefix is a palindrome
                for suf in self.partition(s[i:]):  # process suffix recursively
                    ans.append([s[:i]] + suf)
        return ans
        
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        lst = []
        def palindrome(a):
            return a == a[::-1]
        def dfs(i,curr):
            if i == len(s):
                lst.append(curr)
                return 
            for j in range(i,len(s)):
                sol = s[i:j+1]
                if palindrome(sol):
                    dfs(j+1, curr + [s[i:j+1]])
            return 
        dfs(0,[])
        return lst
            