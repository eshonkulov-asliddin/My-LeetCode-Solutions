from collections import deque
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
#         Linear Search
#         Time Complexity: O(n2)
#         Space Complexity: O(n)
        # ans = []
        # for i in nums:
        #     ans.append(i**2)
        # for i in range(len(ans)):
        #     for j in range(i+1, len(ans)):
        #         if ans[i] > ans[j]:
        #             ans[j], ans[i] = ans[i], ans[j]
        # return ans    
        
#         Two Pointer and built in deque
#         Time Complexity: O(n)
#         Space Complexity: O(n)        
            
#         i, j = 0, len(nums)-1 
#         ans = deque()
        
#         while i <= j:
#             left, right = abs(nums[i]), abs(nums[j])
#             if left > right :
#                 ans.appendleft(left**2)
#                 i += 1
#             else:
#                 ans.appendleft(right**2)
#                 j -= 1
#         return ans 

#         Two Pointer
#         Time Complexity: O(n)
#         Space Complexity: O(n) 
    
        i, j = 0, len(nums)-1 
        ans = [0] * len(nums)
        
        while i <= j:
            left, right = abs(nums[i]), abs(nums[j])
            if left > right :
                ans[j-i] = left**2
                i += 1
            else:
                ans[j-i] = right**2
                j -= 1
        return ans 
    
    