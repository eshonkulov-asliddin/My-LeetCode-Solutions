class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """               
#         Time Complexity: O(n2*2)
#         Space Complexity: O(1)  
#         for i in range(k):
#             n = nums.pop()
#             nums.insert(0, n)

#         Time Complexity: O(n)
#         Space Complexity: O(1)
        # nums[:len(nums)-k], nums[len(nums)-k:] = nums[len(nums)-k:], nums[:len(nums)-k]
            
               
#         Time Complexity: O(n)
#         Space Complexity: O(n)
        # res = [0] * len(nums)
        # for i in range(len(nums)):
        #     if i > k:
        #         res[(i+k) % len(nums)] = nums[i]
        #     else:
        #         res[i+k] = nums[i]
        # return res 
        
#         Time Complexity: O(n)
#         Space Complexity: O(1)

        def helper(start, end, nums):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start+1, end-1
        
        k = k % len(nums )
        l, r = 0, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
            
#         l, r = 0, k-1
#         while l < r:
#             nums[l], nums[r] = nums[r], nums[l]
#             l, r = l+1, r-1   
            
#         l, r = k, len(nums)-1
#         while l < r:
#             nums[l], nums[r] = nums[r], nums[l]
#             l, r = l+1, r-1    
            
        l, r = 0, len(nums)-1            
        helper(l, k-1, nums)
        helper(k, len(nums)-1, nums)
    
            
        