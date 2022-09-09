class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        O(n)
        O(1)
        
        '''
        while True:
            cur = nums[0]
            if nums[0] == nums[cur]:
                return cur
            nums[0], nums[cur] = nums[cur], nums[0]