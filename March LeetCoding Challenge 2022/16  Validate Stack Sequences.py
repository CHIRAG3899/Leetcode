#Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push 
#and pop operations on an initially empty stack, or false otherwise.
#Example 1:
#Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
#Output: true
#Explanation: We might do the following sequence:
#push(1), push(2), push(3), push(4),
#pop() -> 4,
#push(5),
#pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
#Example 2:
#Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
#Output: false
#Explanation: 1 cannot be popped before 2.

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        j = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j == len(popped)
		
class Solution:
    def validateStackSequences(self, pushed, popped):
        ind1, ind2, n = 0, 0, len(pushed)
        stack = []
        while ind1 < n or ind2 < n:
            if stack and stack[-1] == popped[ind2]:
                stack.pop()
                ind2 += 1
            elif ind1 < n:
                stack.append(pushed[ind1])
                ind1 += 1
            else:
                return False
        
        return True