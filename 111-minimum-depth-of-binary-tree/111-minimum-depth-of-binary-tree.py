# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0 
        count = 0
        queue = deque([root])
        while queue:
            lenq = len(queue)
            count += 1
            for i in range(lenq):
                node = queue.popleft()
                if node.left or node.right:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    return count
        
        