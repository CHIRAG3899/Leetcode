Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"

class Solution:
    def removeDuplicateLetters(self, s):
        last_occ = {c: i for i, c in enumerate(s)}
        stack = ["!"]
        Visited = set()
        
        for i, symbol in enumerate(s):
            if symbol in Visited: continue
            
            while (symbol < stack[-1] and last_occ[stack[-1]] > i):
                Visited.remove(stack.pop())
           
            stack.append(symbol)
            Visited.add(symbol)        
        return "".join(stack)[1:]
        