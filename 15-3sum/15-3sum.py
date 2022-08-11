class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Time Complexity: O(n log n + n2)
        Space Complexity: O(1) 
        in some language O(n) as sorting requires additional space
        '''
        
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                
                if threeSum > 0:
                    r -= 1  
                elif threeSum < 0:
                    l += 1  
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res            
        
        
        
        '''
        Brute Force
        Time Complexity: O(n2)
        Space Complexity: O(n)
        '''
#         res = []
#         hel = []
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(j+1, len(nums)):
#                     curInd = [nums[i], nums[j], nums[k]]
#                     curSum = sum(curInd)
#                     if curSum == 0:
#                         hel = sorted([nums[i], nums[j], nums[k]])
#                         if hel not in res:
#                             res.append(hel)
       
#         return res                        