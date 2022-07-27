class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Time Complexity: O(m*n)
        Space Complexity: O(m)
        '''
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return res.values()       