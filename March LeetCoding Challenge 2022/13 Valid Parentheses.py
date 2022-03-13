#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Example 1:
#Input: s = "()"
#Output: true
#Example 2:
#Input: s = "()[]{}"
#Output: true
#Example 3:
#Input: s = "(]"
#Output: false

class Solution:
    def isValid(self, s):
        dct = {"[": "]", "(": ")", "{" : "}"}
        stack = []
        for char in s:
            if char in dct:
                stack.append(char)
            else:
                if not stack or char != dct[stack.pop()]: return False           
        return not stack
        

def isValid(self, s: str) -> bool:
        l = list()
        
        d = {'}':'{', ')':'(', ']':'['}
        b_open = d.values()
        
        for b in s:
            if b in b_open:
                l.append(b)
            else:
                if len(l) > 0 and l[-1] == d[b]:
                        l.pop()
                else:
                    return False
        
        return len(l) == 0