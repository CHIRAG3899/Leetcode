#Given strings s1, s2, and s3, find whether s3 is formed by an interleaving
#of s1 and s2.

#An interleaving of two strings s and t is a configuration where they are
#divided into non-empty substrings such that:

#s = s1 + s2 + ... + sn
#t = t1 + t2 + ... + tm
#|n - m| <= 1
#The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
#Note: a + b is the concatenation of strings a and b.
#Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
#Output: true
#Example 2:Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
#Output: false
#Example 3:Input: s1 = "", s2 = "", s3 = ""
#Output: true

class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        isInterleaved = []
        if len(s3) != len(s1)+len(s2):
            return False
        for i in range(0,len(s1)+1):
            row = []
            for j in range(0,len(s2)+1):
                if i == 0 and  j==0:
                    row.append(True)
                else:
                    temp = False
                    if j>0: 
                        temp = row[j-1] and s3[i+j-1] == s2[j-1]
                    if i>0: 
                        temp = temp or (previousRow[j] and s3[i+j-1] == s1[i-1])
                    row.append(temp)
            previousRow = row
        return row[len(s2)]
