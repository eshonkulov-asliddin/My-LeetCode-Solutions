class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ## Linear Search
        
        index = 0
        for i, v in enumerate(nums):
            if v == target:
                return i 
            if v < target:
                index = i+1
        return index   
                            
            