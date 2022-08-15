class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Time Complexity: O(26 + n) which is O(n)
        Space Complexity: O(n)
        '''
        
        char_freq = {}
        res = 0
        l = 0
        maxf = 0
        
        for r in range(len(s)):
            char_freq[s[r]] = 1 + char_freq.get(s[r], 0)
            maxf = max(maxf, char_freq[s[r]]) 
            
            while (r - l + 1) - maxf > k:
                char_freq[s[l]] -= 1
                l += 1
            res = max(res, r - l +1)  
            
        return res           
                
                       
            
            
            
            