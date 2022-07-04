class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Two Pointer
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        
        l = 0
        for r in range(len(nums)):
            if nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums                