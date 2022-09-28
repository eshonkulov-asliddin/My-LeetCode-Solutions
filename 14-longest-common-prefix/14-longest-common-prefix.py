class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        minX = len(strs[0])
        for i in strs:
            if len(i) < minX:
                minX = len(i)
        prefix = ""
        for i in range(minX):
            for j in range(len(strs)-1):
                if strs[0][i] == strs[j+1][i]:
                    pass
                else:
                    if not prefix: return ""
                    return prefix
            prefix += strs[0][i] 
        return prefix   