#Given the root of a binary tree, return the sum of values of its deepest leaves.
# 
#
#Example 1:
#
#
#Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
#Output: 15
#Example 2:
#
#Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
#Output: 19

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        while queue: # iterates through the layers
            lastSum, newQueue = 0, list() # init sum to zero
            while queue: # current layer's nodes
                node = queue.pop(0)
                lastSum += node.val # sum of the last layer is accumulated here
                if any([node.left, node.right]): # build next layer
                    if node.left: newQueue.append(node.left)
                    if node.right: newQueue.append(node.right)
            queue = newQueue # next layer
        return lastSum
        
from collections import deque
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        queue = deque()
        queue.append(root)
        i = 0
        while queue:
            sum_ = 0;
            n = len(queue)
            i+=1
            for i in range(n):
                node = queue.popleft()
                sum_ += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return sum_
        
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs1(root):
            if not root: return 0
            return max(dfs1(root.left), dfs1(root.right))+1
        def dfs2(root, dep):
            if not root: return
            if dep == max_depth: self.total+= root.val
            dfs2(root.left, dep+1)
            dfs2(root.right, dep+1)
        self.total=0
        max_depth = dfs1(root)
        dfs2(root, 1)
        return self.total
        
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        
        #find maximum depth
        def getHeight(root):
            if not root:
                return 0
            
            return 1 + max(getHeight(root.left), getHeight(root.right))
        
        height = getHeight(root)
        
        total = 0
        
        #Sum all maximum leaves
        def totalSum(root, depth):
            nonlocal total
            if not root:
                return 
            if depth == height:
                total += root.val
                return 
            
        
            totalSum(root.left, depth+1)
            totalSum(root.right, depth+1)
            
            return
        totalSum(root, 1)
        return total