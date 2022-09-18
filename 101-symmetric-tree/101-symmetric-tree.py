# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
                
        def dfs(node1, node2):
            if not node1.left and not node2.right:
                return True
            if node1.left and node2.right and node1.left.val == node2.right.val:
                return ( dfs(node1.left, node2.right) and dfs(node2.right, node1.left) )
            
        ans = dfs(root, root)   
        return ans