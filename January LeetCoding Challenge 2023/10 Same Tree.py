# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True

class Solution:
    # iterative DFS
    def isSameTree(self,p,q):
            stack =[(p,q)]
            while stack:
                p,q = stack.pop()
                if not p and not q:
                    continue
                elif (not p or not q) or (p.val !=q.val):
                    return False
                stack.extend([(q.right,p.right),(q.left,p.left)])
            return True
            
class Solution:
    # iterative BFS
    def isSameTree(self,p,q):
        queue = collections.deque([p,q])
        while queue:
            p,q = queue.popleft()
            if not p and not q:
                continue
            elif (not p or not q) or (p.val != q.val):
                return False
            queue.extend([(p.left,q.left),(p.right,q.right)])
        return True