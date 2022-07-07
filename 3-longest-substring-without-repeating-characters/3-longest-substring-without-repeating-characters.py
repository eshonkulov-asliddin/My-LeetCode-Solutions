class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
#         Sliding Window Algorithm 
#         Time Complexity: O(n)
#         Space Complexity: O(n) 
            
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l +=1
            charSet.add(s[r])
            res = max(res, abs(l-r)+1)
        return res            

                