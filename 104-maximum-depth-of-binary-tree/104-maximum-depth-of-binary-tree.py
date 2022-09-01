# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #recursive
        if not root:
            return 0
        left = 1 + self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)
        return max(left, right)
        
        # bfs
        # if not root:
        #     return 0
        # queue = deque([root])
        # maxDepth = 0
        # while queue:
        #     maxDepth += 1
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return maxDepth  
        
       # dfs iterative
#         if not root:
#             return 0
#         stack = [(root, 1)]
#         maxDepth = 0
#         while stack:
#             node, depth = stack.pop()
#             maxDepth = max(maxDepth, depth)
#             if node.left:
#                 stack.append((node.left, depth + 1))
#             if node.right:
#                 stack.append((node.right, depth + 1))
#         return maxDepth   
                
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            