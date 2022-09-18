# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        if not root: return res
        path = str(root.val)
        if not root.left and not root.right:
            res.append(path)
        if root.left: self.dfs(root.left, path, res) 
        if root.right: self.dfs(root.right, path, res)    
        return res
        
    def dfs(self, node, path, res):
        path += ('->' + str(node.val))
        if not node.left and not node.right:
            res.append(path)
            return
        if node.left: self.dfs(node.left, path, res) 
        if node.right: self.dfs(node.right, path, res)

            
        