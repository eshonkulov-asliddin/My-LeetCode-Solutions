# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        '''
        Recursion
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''

        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()
        
        
        
            
        
            
        
        
        
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