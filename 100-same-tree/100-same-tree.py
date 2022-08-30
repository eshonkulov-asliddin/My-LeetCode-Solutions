# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrder(self, root, res):
        if root:
            res.append(root.val)
            if root.left is None:
                res.append(None)
            res = self.preOrder(root.left, res)
            
            if root.right is None:
                res.append(None)
            res = self.preOrder(root.right, res)
        
            
           
        return res  
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        
        p_l = self.preOrder(p, [])
        q_l = self.preOrder(q, [])
        
        return p_l == q_l
        
        
      
            
                
        