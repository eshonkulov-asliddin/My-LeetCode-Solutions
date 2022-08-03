# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        Floyd's Tortoise and Hare Algorithm
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False    
        
        
        '''
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        d = {}
        
        cur = head
        while cur:
            if not cur in d:
                d[cur] = 1
            else:
                return True
            cur = cur.next
        return False    