class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s = s.lower()
        lenS, ans = len(s), []
        
        def helper(i, res=""):
            if i < lenS:
                helper(i+1, res + s[i])
                if s[i].islower(): helper(i+1, res + s[i].upper())
            else:
                ans.append(res)
        helper(0)
        return ans
                