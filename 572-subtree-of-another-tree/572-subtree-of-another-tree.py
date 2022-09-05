# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        Time Complexity: O(s*t)
        Space Complexiyty: O(1) if not consider the Recursion space
        '''
        if not subRoot: return True
        if not root: return False
        
        if self.isSameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
         
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (self.isSameTree(s.left, t.left) and                                         self.isSameTree(s.right, t.right))
        return False        
        