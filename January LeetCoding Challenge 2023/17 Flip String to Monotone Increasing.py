# A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

# You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

# Return the minimum number of flips to make s monotone increasing.

# Example 1:
# Input: s = "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.

# Example 2:
# Input: s = "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        ones, ans = 0, 0                    # Example: s = "010110"
                                            #
        for num in s:                       #  num    ones   ans  
                                            #  ––––   ––––   ––––  
            if num =='1': ones += 1         #    0      0     0
                                            #    1      1     0
            elif ones:                      #    0      0     1
                ones -= 1                   #    1      1     1
                ans += 1                    #    1      2     1
                                            #    0      1     2
        return ans
        
class Solution(object):
    def minFlipsMonoIncr(self, s):
        ones = 0
        flips = 0
        
        for c in s:
            if c == '0'and ones > 0:
                flips += 1
                ones -= 1
            elif c == '1':
                ones += 1
        
        return flips