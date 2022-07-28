class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Time Complexity: O(n*m)
        Space Complexity: O(n*m)
        
        '''
        d = dict()
        res = []
        for i in nums:
            d[i] = 1 + d.get(i, 0)
                
        while k > 0:
            max_elem = max(d, key=d.get)
            res.append(max_elem)
            d[max_elem] = 0
            k -= 1
        return res                