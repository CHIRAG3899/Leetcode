#Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.
#
# 
#
#Example 1:
#
#Input: s = "00110110", k = 2
#Output: true
#Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
#Example 2:
#
#Input: s = "0110", k = 1
#Output: true
#Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
#Example 3:
#
#Input: s = "0110", k = 2
#Output: false
#Explanation: The binary code "00" is of length 2 and does not exist in the array.

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        got = set()

        for i in range(k, len(s)+1):
            tmp = s[i-k:i]
            if tmp not in got:
                got.add(tmp)
                need -= 1
                # return True when found all occurrences
                if need == 0:
                    return True
        return False
        
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        got = [False]*need
        all_one = need - 1
        hash_val = 0

        for i in range(len(s)):
            # calculate hash for s[i-k+1:i+1]
            hash_val = ((hash_val << 1) & all_one) | (int(s[i]))
            # hash only available when i-k+1 > 0
            if i >= k-1 and got[hash_val] is False:
                got[hash_val] = True
                need -= 1
                if need == 0:
                    return True
        return False