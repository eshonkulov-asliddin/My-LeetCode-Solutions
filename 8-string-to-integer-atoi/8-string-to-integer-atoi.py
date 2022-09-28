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
        
        num = ""
        while i < len(s):
            if not s[i].isdigit():
                break
            num += s[i]   
            i += 1
            
        if not num:
            return 0
        if int(num) >= 2147483648 and sign == -1:
            num = 2147483648 
        elif int(num) >= 2147483648:
            num = 2147483648 - 1 
        return int(num) * sign   
                
                