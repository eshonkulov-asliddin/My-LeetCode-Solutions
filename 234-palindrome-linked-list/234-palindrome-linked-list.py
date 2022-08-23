# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        values = []
        cur = head
        while cur:
            values.append(cur.val)
            cur = cur.next
        return values == values[::-1]    