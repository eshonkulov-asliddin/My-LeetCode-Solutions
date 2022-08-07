# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
[9,9,9,9,9,9,9]
[9,9,9,9]

[8,9,9,9,0,0,0,1 ]

'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
#         dummy = ListNode()
#         cur = dummy
#         carry = 0           
            
#         while l1 or l2 or carry:
#             v1 = l1.val if l1 else 0
#             v2 = l2.val if l2 else 0
            
#             val = v1 + v2 + carry
#             carry = val // 10
#             val %= 10
                
                
            
#             cur.next = ListNode(val)
            
#             #update
#             cur = cur.next
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
            
#         return dummy.next        
                 
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        l1_str = ''
        l2_str = ''
        while l1 or l2:
            if l1:
                l1_str += str(l1.val)
            if l2:
                l2_str += str(l2.val)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        output = str(int(l1_str[::-1]) + int(l2_str[::-1]))
        # print(type(output))
        
        dummy = ListNode()
        cur = dummy
        
        
        for i in reversed(output):
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next    