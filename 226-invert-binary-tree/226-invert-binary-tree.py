# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left and node.right:
                tmp = node.left
                node.left = node.right
                node.right = tmp
                stack.append(node.left)
                stack.append(node.right)
            elif node.left:
                node.right = node.left
                node.left = None
                stack.append(node.right)
            elif node.right:
                node.left = node.right
                node.right = None
                stack.append(node.left)
                
            
        
        return root