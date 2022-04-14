#You are given the root of a binary search tree (BST) and an integer val.
#
#Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
#
#Example 1:
#Input: root = [4,2,7,1,3], val = 2
#Output: [2,1,3]
#Example 2:
#Input: root = [4,2,7,1,3], val = 5
#Output: []

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp=root
        while(temp!=None):
            if temp.val==val:
                return temp
            elif val>temp.val:
                temp=temp.right
            else:
                temp=temp.left
        return None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # iterative solution
        while root is not None:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            elif val == root.val:
                return root
        return None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # Recursive solution
        if root is None or val == root.val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)