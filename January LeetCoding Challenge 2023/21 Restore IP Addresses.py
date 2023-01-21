# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

# Example 1:
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]

# Example 2:
# Input: s = "0000"
# Output: ["0.0.0.0"]

# Example 3:
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.recurse(s, ans, 0, "", 0)
        return ans
    
    def recurse(self, curr, ans, index, temp, count):
        if count > 4:
            return
        if count == 4 and index == len(curr):
            ans.append(temp)
        for i in range(1, 4):
            if index + i > len(curr):
                break
            s = curr[index:index+i]
            if (s.startswith("0") and len(s) > 1) or (i == 3 and int(s) >= 256):
                continue
            self.recurse(curr, ans, index+i, temp + s + ("." if count < 3 else ""), count+1)
            
