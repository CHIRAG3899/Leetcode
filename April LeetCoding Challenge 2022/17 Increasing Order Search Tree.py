Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
Example 1:
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:
Input: root = [5,1,7]
Output: [1,null,5,null,7]

class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right

class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right

class Solution:
    def increasingBST(self, root):
        def dfs(node):
            l1, r2 = node, node
            
            if node.left: 
                l1, l2 = dfs(node.left)
                l2.right = node
                
            if node.right:
                r1, r2 = dfs(node.right)
                node.right = r1
            
            node.left = None
            return (l1, r2)
        
        return dfs(root)[0]

