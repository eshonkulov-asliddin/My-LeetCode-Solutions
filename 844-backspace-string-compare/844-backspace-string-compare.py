class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool: 
        s = self.build(s)
        t = self.build(t)
        return s == t
    
    def build(self, st):
        stack = []
        for i in range(len(st)):
            if st[i] == '#':
                if stack:
                    stack.pop()
                continue
            stack.append(st[i])
        return stack  
        
        
        
                