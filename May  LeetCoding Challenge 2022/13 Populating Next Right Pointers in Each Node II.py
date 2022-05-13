#Given a binary tree
#
#struct Node {
#  int val;
#  Node *left;
#  Node *right;
#  Node *next;
#}
#Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
#Initially, all next pointers are set to NULL.
#
# 
#
#Example 1:
#
#
#Input: root = [1,2,3,4,5,null,7]
#Output: [1,#,2,3,#,4,5,7,#]
#Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
#Example 2:
#
#Input: root = []
#Output: []

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        def helper( node: 'Node'):
            
            if not node:
                return None
            
            scanner = node.next

            # Scanner finds left-most neighbor, on same level, in right hand side
            while scanner:

                if scanner.left:
                    scanner = scanner.left
                    break

                if scanner.right:
                    scanner = scanner.right
                    break

                scanner = scanner.next


            # connect right child if right child exists
            if node.right:
                node.right.next = scanner 

            # connect left child if left child exists
            if node.left:
                node.left.next = node.right if node.right else scanner


            # DFS down to next level
            helper( node.right )  
            helper( node.left )  
                
            return node
        # -------------------------------
        
        return helper( root )


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        toprow = root
        while toprow:
            start = cur = Node()
            top = toprow
            while top:
                for child in [top.left, top.right]:
                    cur.next = child
                    if cur.next: 
                        cur = cur.next
                top = top.next
                toprow = start.next
        return root