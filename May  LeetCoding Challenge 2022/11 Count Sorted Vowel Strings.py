#Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.
#
#A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.
#
# 
#
#Example 1:
#
#Input: n = 1
#Output: 5
#Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
#Example 2:
#
#Input: n = 2
#Output: 15
#Explanation: The 15 sorted strings that consist of vowels only are
#["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
#Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
#Example 3:
#
#Input: n = 33
#Output: 66045

class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[i for i in range(5,0,-1)] for _ in range(n)]   # intialize dp matrix
        
        for i in range(1,n):
            for j in range(3,-1,-1):
                dp[i][j] = dp[i - 1][j] + dp[i][j + 1]   # dp expression
                
        return dp[n-1][0]

class Solution:
    def countVowelStrings(self, n: int) -> int:
        def count(n,vow):
            if vow == 0: return 0
            if n == 0: return 1
            return count(n,vow-1)+count(n-1,vow)
        return count(n,5)

class Solution:
    def countVowelStrings(self, n: int) -> int:
        def count(n,vow):
            if vow == 0: 
                mem[n][vow] =  0
                return mem[n][vow]
            if n == 0: 
                mem[n][vow] = 1
                return mem[n][vow]
            if mem[n][vow]!=-1:
                return mem[n][vow]
            mem[n][vow] = count(n,vow-1)+count(n-1,vow)
            return mem[n][vow]
        mem = [[-1]*6 for i in range(n+1)]
        return count(n,5)