# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # bfs
        if not root:
            return 0
        queue = deque([root])
        maxDepth = 0
        while queue:
            maxDepth += 1
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return maxDepth            
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
                
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # if not root:
        #     return 0
#         else:
#             return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

            
# #         stack = [root]
# #         level = 0
        
# #         while len(stack) > 0:
            
# #             for i in range(len(stack)):
# #                 node = stack.pop(0)
                
            
# #                 if node.left:
# #                     stack.append(node.left)
# #                 if node.right:
# #                     stack.append(node.right)
# #             level += 1    
          
            
# #         return level

#         stack = [[root, 1]]
#         res = 0
        
#         while stack:
#             node, depth = stack.pop()
#             if node:
#                 res = max(res, depth)
#                 stack.append([node.left, depth+1])
#                 stack.append([node.right, depth+1])
#         return res        

                
                
                
                
                
                
                
                
                
                
            