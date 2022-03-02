#Given two strings s and t, return true if s is a subsequence of t, or
#false otherwise.

#A subsequence of a string is a new string that is formed from the original
#string by deleting some (can be none) of the characters without disturbing
#the relative positions of the remaining characters. (i.e., "ace" is a
#subsequence of "abcde" while "aec" is not).

 

#Example 1:

#Input: s = "abc", t = "ahbgdc"
#Output: true
#Example 2:

#Input: s = "axc", t = "ahbgdc"
#Output: false


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j, n, m = 0, 0, len(s), len(t)
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1 
            j += 1 # Update j always.
        return i == n

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):return False
        if len(s) == 0:return True
        subsequence=0
        for i in range(0,len(t)):
            if subsequence <= len(s) -1:
                print(s[subsequence])
                if s[subsequence]==t[i]:

                    subsequence+=1
        return  subsequence == len(s)
