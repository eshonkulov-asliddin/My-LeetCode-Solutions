class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        
        i = 0
        if not s:
            return 0
        
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        parsed = 0
        while i < len(s):
            cur = s[i]  
            if not cur.isdigit():
                break
            parsed = parsed * 10 + int(cur) 
            i += 1
            
        parsed *= sign
        if parsed > 2 ** 31-1:
            return 2 ** 31 -1
        elif parsed < -2 ** 31:
            return -2 ** 31
        else:
            return parsed
                
                