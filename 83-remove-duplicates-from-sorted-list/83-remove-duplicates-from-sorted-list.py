# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return
        
        dummy = ListNode(next=head)
        prev = dummy.next
        cur = head.next
        
        while cur:
            nxt = cur.next
            if prev.val == cur.val:
                prev.next = cur.next
            else:
                prev = cur
            cur = nxt
            
        return dummy.next     
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         cur = head
        
#         while cur:
#             while cur.next and cur.next.val == cur.val:
#                 cur.next = cur.next.next
#             cur = cur.next
            
#         return head
            
        
        
#         l = []
#         while head:
#             l.append(head.val)
#             head = head.next
           
#         l = list(dict.fromkeys(l))
#         final_res = None
        
#         for i in l[::-1]:
#             final_res = ListNode(val=i, next=final_res)
#         return final_res    
