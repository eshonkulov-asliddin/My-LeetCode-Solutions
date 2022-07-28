class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Time Complexity:
        Space Complexity:
        
        '''
        d = dict()
        res = []
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                
        while k > 0:
            max_elem = max(d, key=d.get)
            res.append(max_elem)
            d[max_elem] = 0
            k -= 1
        return res                