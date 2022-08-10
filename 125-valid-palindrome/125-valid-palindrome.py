class Solution:
    def alphaNum(self, c):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))
        
    def isPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s)-1
        
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
                
            if s[l].lower() != s[r].lower():
                return False
            
            l, r = l + 1, r - 1
        return True    
        
        '''
        Two Pointer Without using built in function isalnum()
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        
        
         
                            
                    
        '''
        Two Pointer
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
#         r = len(s)-1
#         l = 0
        
#         while l < r:
#             if not s[l].isalnum():
#                 l += 1
#                 continue
#             if not s[r].isalnum():
#                 r -= 1
#                 continue 
#             if s[l].lower() != s[r].lower():
#                 return False 
            
#             l += 1
#             r -= 1
#         return True  

       

        
        '''
        Time Complexity: 
        Space Complexity:
        '''
#         s = "".join(i.lower() for i in s if i.isalnum())
        
#         return s == s[::-1]