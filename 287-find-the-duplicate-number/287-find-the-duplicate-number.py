class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        d = dict()
        for idx, val in enumerate(nums):
            if val not in d:
                d[val] = idx
                continue
            return val    