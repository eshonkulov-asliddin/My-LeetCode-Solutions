class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        
        s1Count = [0] * 26
        s2Count = [0] * 26
        
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
            
        matches = 0
        
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
                
        l = 0
        for r in range(len(s1), len(s2)):
            
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            
            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
                
             # leftside will be deleted
            
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s2Count[index] == s1Count[index] - 1:
                matches -= 1
                
            l += 1
        return matches == 26           
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Time Complexity: O(n)
        # Space Complexity: O(1)  
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26 

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches +=1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            #leftside which will be deleted
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1  
                
            l += 1
            
        return  matches == 26 
        
        
#         if len(s1) > len(s2):
#             return False
        
#         s1Count, s2Count = [0] * 26, [0] * 26
#         for i in range(len(s1)):
#             s1Count[ord(s1[i]) - ord('a')] +=1
#             s2Count[ord(s2[i]) - ord('a')] +=1
                    
#         matches = 0
#         for i in range(26):
#             matches += (1 if s1Count[i] == s2Count[i] else 0)  
            
#         l = 0
#         for r in range(len(s1), len(s2)):
#             if matches == 26: return True
            
#             index = ord(s2[r]) - ord('a')
#             s2Count[index] += 1
#             if s1Count[index] == s2Count[index]:
#                 matches += 1
#             elif s1Count[index] + 1 == s2Count[index]:
#                 matches -= 1
             
#             #left side
#             index = ord(s2[l]) - ord('a')
#             s2Count[index] -= 1
#             if s1Count[index] == s2Count[index]:
#                 matches += 1
#             elif s1Count[index] - 1 == s2Count[index]:
#                 matches -= 1 
#             l += 1
            
                
#         return matches == 26  

                