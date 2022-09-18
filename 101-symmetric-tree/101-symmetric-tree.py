# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        stack = [(root, root)]
        isTrue = True
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            if node1.val != node2.val:
                return False
            if node1.left and node2.right or not node1.left and not node2.right:
                stack.append((node1.left, node2.right))
            elif not node1.left or not node2.right:
                return False
            if node1.right and node2.left or not node1.right and not node2.left:
                stack.append((node1.right, node2.left))
            elif not node1.right or not node2.left:
                return False    
            
                
           
        return True          
                
                    
        