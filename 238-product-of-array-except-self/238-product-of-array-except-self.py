
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Time Complexity: O(n)
        Space Complexity: O(1)

        '''
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res    
            
            
            
        '''
        Time Complexity: O(n2)
        Space Complexity: O(1)
        '''
#         res = []
#         for i in range(len(nums)):
#             product = 1
#             for j in range(len(nums)):
#                 if j != i:
#                     product *= nums[j]
#             res.append(product)
#         return res    
                    
            