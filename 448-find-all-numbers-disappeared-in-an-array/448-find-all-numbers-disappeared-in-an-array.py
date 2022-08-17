class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''
        Hashing
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        d = {}
        for i in nums:
            d[i] = 1 + d.get(i, 0)
        res = []
        for i in range(1, len(nums)+1):
            if i not in d:
                res.append(i)
        return res                