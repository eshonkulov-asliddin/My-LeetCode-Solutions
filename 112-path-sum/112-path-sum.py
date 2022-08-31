# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
        Time Complexity: O(n)
        Space complexity: worst case: O(n) else: O(log n)
        '''
        # iterative
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, curSum = stack.pop()
            
            if not node.left and not node.right:
                if curSum == targetSum:
                    return True
            else:
                if node.left:
                    stack.append((node.left, curSum+node.left.val))
                if node.right:
                    stack.append((node.right, curSum+node.right.val))  
        return False        
        
        # recursive
#         def dfs(node, curSum):
#             if not node:
#                 return False
#             curSum += node.val
            
#             if not node.left and not node.right:
#                 return curSum == targetSum
            
#             return (dfs(node.left, curSum) or
#                     dfs(node.right, curSum))
#         return dfs(root, 0)
    