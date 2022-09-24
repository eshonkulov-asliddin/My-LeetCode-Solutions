class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        
        """
        
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        res = 0
        temp = 0
        for i in range(len(s)-1, -1, -1):
            cur = roman[s[i]]
            if cur >= temp:
                res += cur
                temp = cur
            else:
                res -= cur
                temp = cur
        return res        
                
        
#         output = 0
#         for i in range(len(s)-1):
#             if roman[s[i]] >= roman[s[i+1]]:
#                 cur = roman[s[i]]
#                 output += cur
#             else:
#                 cur = roman[s[i]] * -1
#                 output += cur
        
#         output += roman[s[-1]]
        
#         return output        
                