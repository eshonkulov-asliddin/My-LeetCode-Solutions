class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Time Complexity: O(n*m)
        Space Complexity: O(n*m)
        
        '''
#         d = dict()
#         res = []
#         for i in nums:
#             d[i] = 1 + d.get(i, 0)
                
#         while k > 0:
#             max_elem = max(d, key=d.get)
#             res.append(max_elem)
#             d[max_elem] = 0
#             k -= 1
#         return res 


        # Time Complexity: O(n)
        # Space Complexity: O(n)
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res