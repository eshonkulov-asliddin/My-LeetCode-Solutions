class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Two Pointer Aproach
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        p = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[p] = nums[i+1]
                p += 1
        return p        
              