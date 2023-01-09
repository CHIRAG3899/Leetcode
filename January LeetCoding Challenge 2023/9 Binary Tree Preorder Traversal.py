# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,2,3]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:

                                            #  Ex: root = [1, 2,None, 3,4]
        if not root: return []              #         __1
        stack, ans = [root], []             #        /
                                            #       2
        while stack:                        #      / \
            node = stack.pop()              #     3   4
            ans.append(node.val)            #
                                            #     node     node.left   node.right  stack    ans
            if node.right:                  #   –––––––––  –––––––––   –––––––––   ––––––  ––––––
                stack.append(node.right)    #                                       [1]     []
            if node. left:                  #       1          2         None       [2]     [1]
                stack.append(node.left )    #       2          3          4         [4,3]   [1,2]
                                            #       3        None        None       [4]     [1,2,3]
                                            #       4        None        None       [4]     [1,2,3,4]
        return ans
        
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		# root -> left  -> right
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        ret = []
        def dfs(node):
            if not node:
                return
            ret.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ret

class Solution:
	"""
	Time:   O(n)
	Memory: O(n)
	"""

	def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		return list(self.preorder_generator(root))

	@classmethod
	def preorder_generator(cls, tree: Optional[TreeNode]):
		if tree is not None:
			yield tree.val
			yield from cls.preorder_generator(tree.left)
			yield from cls.preorder_generator(tree.right)
