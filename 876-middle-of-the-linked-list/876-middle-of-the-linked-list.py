# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow    
    
    
    
    
    # Time Complexity: O(n log n)
        # Space Complexity: O(1)   
        
#         cur = head
#         count = 0
#         while cur:
#             count +=1
#             cur = cur.next
            
#         cur = head
#         mid = count // 2
#         while cur and mid != 0:
#             cur = cur.next
#             mid -=1
#         head = cur  
#         return head

      
    
    
    
    
    
    
    
    
    
    
    
    
    
    