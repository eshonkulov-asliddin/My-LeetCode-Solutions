# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        len_list = 0
        cur = head
        while cur:
            len_list += 1
            cur = cur.next
            
        if len_list <= 1:
            return 
        elif len_list == 2:
            if n == 1:
                cur = head
                cur.next = None
            else:
                head = head.next
            return head
        elif len_list == n:
            head = head.next
            return head
        else:
            cur = head
            prev = None

            while cur and len_list != n:
                prev = cur
                cur = cur.next
                len_list -=1

            prev.next = cur.next 
            cur =None

            return head