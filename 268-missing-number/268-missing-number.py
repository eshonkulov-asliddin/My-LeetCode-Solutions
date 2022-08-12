class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
    #Math
        n = len(nums)
        expected = n * (n+1) // 2
        actual = sum(nums)
        return expected - actual
    
    
    
#         sum_n = 0
#         for i in range(len(nums)+1):
#             sum_n += i
            
#         return sum_n - sum(nums)  
    
        '''
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
#         d = dict()
#         for i in range(len(nums)+1):
#             d[i] = 1
            
#         for i in nums:
#             if i in d:
#                 d[i] = 0
         
#         for k, v in d.items():
#             if v != 0:
#                 return k
        
        
