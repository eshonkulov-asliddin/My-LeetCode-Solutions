class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
##Linear Search##
# Time Complexity: O(n)#
#Space Complexity: O(1)#
        
#         for i, k in enumerate(nums):
#             if k == target:
#                 return i
#         return -1    


##Binary Search##
# Time Complexity: O(log n)#
#Space Complexity: O(1)#

        low = 0
        high = len(nums) -1
        
        while low <= high:
            mid = (high + low) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1       
                