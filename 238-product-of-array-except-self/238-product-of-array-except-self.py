
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        [1, 2, 3, 4]
        
        prefix = 1
        loop:
            prefix *= nums[i]
        [1, 1, 2, 6]
        
        postfix = 1
        loop:
            postfix *= nums[i]
        [24, 12, 8, 6]
        
        
        [ ,24]
        '''
        
        
        res = [0]* len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res    