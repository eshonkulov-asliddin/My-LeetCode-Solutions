# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = {}
        
        cur = head
        while cur:
            if not cur in d:
                d[cur] = 1
            else:
                return True
            cur = cur.next
        return False    