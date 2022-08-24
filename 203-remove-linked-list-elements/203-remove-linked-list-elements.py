# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        
        dummy = ListNode(next=head)
        prev = dummy
        cur = head
        
        while cur:
            nxt = cur.next
            
            if cur.val == val:
                prev.next = nxt
            else:
                prev = cur
            cur = cur.next
                
        return dummy.next  
    
    
    
#         dummy_head = ListNode(-1)
#         dummy_head.next = head
        
#         current_node = dummy_head
#         while current_node.next != None:
#             if current_node.next.val == val:
#                 current_node.next = current_node.next.next
#             else:
#                 current_node = current_node.next
                
#         return dummy_head.next
            
            
            