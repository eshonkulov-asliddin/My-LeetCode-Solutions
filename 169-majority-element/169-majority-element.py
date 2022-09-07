class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Time Complexity: O(n+m)
        Space Complexity: O(n)
        '''
        d = {}
        maxCount, res = 0, 0
        for num in nums:
            d[num] = 1 + d.get(num, 0)
            res = num if d[num] > maxCount else res
            maxCount = max(d[num], maxCount)
        return res
        
        