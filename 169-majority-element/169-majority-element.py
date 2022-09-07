class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        
        for num in nums:
            d[num] = 1 + d.get(num, 0)
        
        majority = len(nums) // 2
        for k, v in d.items():
            if v > majority:
                return k
        