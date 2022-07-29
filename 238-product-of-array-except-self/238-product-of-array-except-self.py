import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        n = len(nums)
        # Base case
        if(n == 1):
            print(0)
            return

        # Allocate memory for temporary arrays left[] and right[]
        left = [0]*n
        right = [0]*n

        # Allocate memory for the product array
        prod = [0]*n

        # Left most element of left array is always 1
        left[0] = 1

        # Right most element of right array is always 1
        right[n - 1] = 1

        # Construct the left array
        for i in range(1, n):
            left[i] = nums[i - 1] * left[i - 1]

        # Construct the right array
        for j in range(n-2, -1, -1):
            right[j] = nums[j + 1] * right[j + 1]

        # Construct the product array using
        # left[] and right[]
        for i in range(n):
            prod[i] = left[i] * right[i]

        return prod

        
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
                    
            