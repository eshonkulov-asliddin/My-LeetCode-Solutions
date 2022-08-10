class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        '''
        Two Pointer
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        
        r = len(s)-1
        l = 0
        
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue 
            if s[l].lower() != s[r].lower():
                return False 
            
            l += 1
            r -= 1
        return True    
           
        
        '''
        Time Complexity: 
        Space Complexity:
        '''
#         s = "".join(i.lower() for i in s if i.isalnum())
        
#         return s == s[::-1]