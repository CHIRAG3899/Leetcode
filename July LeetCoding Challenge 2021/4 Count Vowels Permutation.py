#Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
#Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
#Each vowel 'a' may only be followed by an 'e'.
#Each vowel 'e' may only be followed by an 'a' or an 'i'.
#Each vowel 'i' may not be followed by another 'i'.
#Each vowel 'o' may only be followed by an 'i' or a 'u'.
#Each vowel 'u' may only be followed by an 'a'.
#Since the answer may be too large, return it modulo 10^9 + 7.
#Example 1:
#Input: n = 1
#Output: 5
#Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
#Example 2:
#Input: n = 2
#Output: 10
#Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
#Example 3: 
#Input: n = 5
#Output: 68

import numpy as np

class Solution:
    def countVowelPermutation(self, n): 
        def power(mat, n, M):
            result = np.eye(len(mat), dtype = int)
            while n > 0:
                if n%2: result = np.dot(mat, result) % M
                mat = np.dot(mat, mat) % M
                n //= 2
            return result
        
        M = 10**9 + 7
        mat = np.matrix([[0,1,0,0,0], [1,0,1,0,0], [1,1,0,1,1], [0,0,1,0,1], [1,0,0,0,0]])      
        return np.sum(power(mat, n-1, M)) % M
