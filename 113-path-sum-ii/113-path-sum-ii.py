# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return
        res = []
#         def dfs(node, ans):
#             if not node.left and not node.right:
#                 if sum(ans) == targetSum:
#                     res.append(ans)
#             if node.left:
#                 return dfs(node.left, ans+[node.left.val])
#             if node.right:
#                 return dfs(node.right, ans+[node.right.val])
            
#         dfs(root, [root.val]) 
#         return res
        stack = [(root, [root.val])]
        res = []
        ans = []
        while stack:
            node, ans = stack.pop()

            if not node.left and not node.right:
                if sum(ans) == targetSum:
                    res.append(ans)

                    
            if node.left:
                stack.append((node.left, ans+[node.left.val]))
            if node.right:
                stack.append((node.right, ans+[node.right.val]))
        return res         
                    
                
            