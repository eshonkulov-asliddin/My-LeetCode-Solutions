from collections import deque
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        '''
        [-4,-1,0,3,10]
         -> 
        
        res = [121, 9, 9,  4, 49,  ]
        
        
        '''
        l, r = 0, len(nums)-1
        res = []
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res.append(abs(nums[l]) ** 2)
                l += 1
            else:
                res.append(abs(nums[r]) ** 2)
                r -= 1
        return res[::-1]        
            
                    