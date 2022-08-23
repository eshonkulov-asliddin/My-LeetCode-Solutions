# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
 
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
       
        if not head:
            return True
                
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse(first_half_end.next)
        
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next
            
        first_half_end.next = self.reverse(second_half_start)  
        return result
    
    
    def end_of_first_half(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow 
        
    def reverse(self, start):
        prev = None
        cur = start
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
            
        
        '''
        Recursion
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''

#         self.front_pointer = head

#         def recursively_check(current_node=head):
#             if current_node is not None:
#                 if not recursively_check(current_node.next):
#                     return False
#                 if self.front_pointer.val != current_node.val:
#                     return False
#                 self.front_pointer = self.front_pointer.next
#             return True

#         return recursively_check()
        
        
        
            
        
            
        
        
        
        '''
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        # values = []
        # cur = head
        # while cur:
        #     values.append(cur.val)
        #     cur = cur.next
        # return values == values[::-1]    