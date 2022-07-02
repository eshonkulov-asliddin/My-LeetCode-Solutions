class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        
        ## Binary Search
        ## Time Complexity: O(log n)
        ## Space Complexity: O(1)
        low = 0 
        high = len(nums) - 1
        index = 0
        
        while low <= high:
            mid = (high+low) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                index = mid+1
        return index        
        
        ## Linear Search
        ## Time Complexity: O(n)
        ## Space Complexity: O(1)
        
        # index = 0
        # for i, v in enumerate(nums):
        #     if v == target:
        #         return i 
        #     if v < target:
        #         index = i+1
        # return index   
                            
            