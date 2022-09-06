class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        O(n)
        O(n)
        '''
        d = dict()
        for idx, val in enumerate(nums):
            if val in d:
                return [idx, d[val]]
            curKey = target - val
            d[curKey] = idx
        
        