#Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

#Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

#Example 1:

#Input: root = [1,0,2], low = 1, high = 2
#Output: [1,null,2]
#Example 2:

#Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
#Output: [3,2,null,1]

class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        def trim(node):
            if not node:
                return None
            elif node.val > high:
                return trim(node.left)
            elif node.val < low:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)

class Solution:
   def trimBST(self, root, low, high):
       def dfs(node):
           if not node: return node
           if node.val > high:
               return dfs(node.left)
           elif node.val < low:
               return dfs(node.right)
           else:
               node.left  = dfs(node.left)
               node.right = dfs(node.right)
               return node
           
       return dfs(root)