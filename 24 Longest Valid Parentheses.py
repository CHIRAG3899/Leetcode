#Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#
# 
#
#Example 1:
#
#Input: s = "(()"
#Output: 2
#Explanation: The longest valid parentheses substring is "()".
#Example 2:
#
#Input: s = ")()())"
#Output: 4
#Explanation: The longest valid parentheses substring is "()()".
#Example 3:
#
#Input: s = ""
#Output: 0

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [0,] # Initial value to handle "()"
        max_parenthesis = 0
        for bracket in s:
            if bracket == '(':
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2  # Add 2 when a ")" matches "("
                    max_parenthesis = max(max_parenthesis, stack[-1]) # Keep track of longest valid sequence
                else:
                    stack = [0]

        return max_parenthesis
        
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        ending_here = len(s) * [0]
        res, x = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                x += 1
            else:
                if x > 0:
                    x -= 1
                    j = i - 1 - ending_here[i-1]
                    if s[j] == '(':
                        ending_here[i] = ending_here[i-1] + 2
                        if j-1 >= 0:
                            ending_here[i] += ending_here[j-1]
                        res = max(res, ending_here[i])
        return res