# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashmap = {}
        curA = headA
        while curA:
            hashmap[curA] = 1
            curA = curA.next
        
        curB = headB
        while curB:
            if curB in hashmap:
                
                return curB
            hashmap[curB] = 1
            curB = curB.next
        return None