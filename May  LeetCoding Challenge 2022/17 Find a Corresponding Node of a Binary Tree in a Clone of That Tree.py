#Given two binary trees original and cloned and given a reference to a node target in the original tree.
#
#The cloned tree is a copy of the original tree.
#
#Return a reference to the same node in the cloned tree.
#
#Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.
#
#Example 1:
#
#Input: tree = [7,4,3,null,null,6,19], target = 3
#Output: 3
#Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.
#Example 2:
#
#Input: tree = [7], target =  7
#Output: 7
#Example 3:
#
#Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
#Output: 4

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def inorder(o: TreeNode, c: TreeNode):
            if o:
                inorder(o.left, c.left)
                if o is target:
                    self.ans = c
                inorder(o.right, c.right)
                
        inorder(original, cloned)
        return self.ans 
        

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack_o, stack_c = [], []
        node_o, node_c = original, cloned
        
        while stack_o or node_c:
            while node_o:
                stack_o.append(node_o)
                stack_c.append(node_c)
                
                node_o = node_o.left
                node_c = node_c.left
                
            node_o = stack_o.pop()
            node_c = stack_c.pop()
            
            if node_o is target:
                return node_c
            
            node_o = node_o.right
            node_c = node_c.right
            

