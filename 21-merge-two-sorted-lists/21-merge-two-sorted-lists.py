# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if not list1 and not list2:
            return
        
        l1 = list1
        l2 = list2
        q = None
        
        if not l1 :
            return l2
        if not l2:
            return l1
        
        if l1 and l2:
            if l1.val <= l2.val:
                q = l1
                l1 = q.next
            else:
                q = l2
                l2 = q.next
            new_head = q
            
        while l1 and l2:
            if l1.val <= l2.val:
                q.next = l1
                q = l1
                l1 = q.next
            else:
                q.next = l2
                q = l2
                l2 = q.next
               
        if l1 is None:
            q.next = l2
        if l2 is None:
            q.next = l1
        self.head = new_head
        return self.head   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         l1 = list1
#         l2 = list2
#         q = None
        
#         if l1 is None:
#             return l2
#         if l2 is None:
#             return l1
        
#         if l1 and l2:
#             if l1.val <= l2.val:
#                 q = l1
#                 l1 = q.next
#             else:
#                 q = l2
#                 l2 = q.next
#             new_head = q
           
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 q.next = l1
#                 q = l1
#                 l1 = q.next
#             else:
#                 q.next = l2
#                 q = l2
#                 l2 = q.next
               
#         if l1 is None:
#             q.next = l2
#         if l2 is None:
#             q.next = l1
#         self.head = new_head
#         return self.head
        
#         l1 = []
#         l2 = []
#         while list1:
#             l1.append(list1.val)
#             list1 = list1.next
            
#         while list2:
#             l2.append(list2.val)
#             list2 = list2.next
           
#         res= l1+l2
#         res.sort()
        
#         final_res = None
        
#         for i in res[::-1]:
#             final_res = ListNode(val=i, next=final_res)
            
        # return final_res
        
    
     