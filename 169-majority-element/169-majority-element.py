class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        res, count = 0, 0
        for num in nums:
            if num != res:
                if count:
                    count -= 1
                else:
                    res = num
                    count = 1
            else:
                count += 1
        return res        
        # d = {}
        # maxCount, res = 0, 0
        # for num in nums:
        #     d[num] = 1 + d.get(num, 0)
        #     res = num if d[num] > maxCount else res
        #     maxCount = max(d[num], maxCount)
        # return res
        
        