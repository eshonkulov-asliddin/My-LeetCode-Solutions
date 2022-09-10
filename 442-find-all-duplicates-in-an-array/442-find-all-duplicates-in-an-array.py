class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        unique = set()
        for num in nums:
            if num in unique:
                res.append(num)
            unique.add(num)
        return res    