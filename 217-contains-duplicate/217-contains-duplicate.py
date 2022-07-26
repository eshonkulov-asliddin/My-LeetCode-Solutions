class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            hashmap[nums[i]] = i
        return False    