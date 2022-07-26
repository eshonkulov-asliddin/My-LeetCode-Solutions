class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        
        # Time Complexity: O(n log n)
        # Space Complexity: O(1)
       
        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]] += 1
            else:    
                hashmap[s[i]] = 1
            
            
        for i in range(len(t)):
            if t[i] in hashmap:
                hashmap[t[i]] -= 1
            else:
                return False
            
        for i in hashmap:
            if hashmap[i] != 0:
                return False
        return True    
        
        
        '''
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        '''
        
        # return sorted(s) == sorted(t) 
        
        
                    