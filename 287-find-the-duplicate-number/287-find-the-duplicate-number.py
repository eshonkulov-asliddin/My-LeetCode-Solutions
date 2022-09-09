class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        O(n)
        O(1)
        
        '''
        def store(nums, cur):
            if cur == nums[cur]:
                return cur
            nxt = nums[cur]
            nums[cur] = cur
            return store(nums, nxt)
        return store(nums, 0)