class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def apply(s):
            backspace = 0
            for i in range(len(s)-1, -1, -1):
                if s[i] == '#':
                    backspace += 1
                elif backspace:
                    backspace -= 1
                else:
                    yield s[i]
        return all(x==y for x, y in zip_longest(apply(s), apply(t) ) )            
        
        
#         s = self.build(s)
#         t = self.build(t)
#         return s == t
    
#     def build(self, st):
#         stack = []
#         for i in range(len(st)):
#             if st[i] == '#':
#                 if stack:
#                     stack.pop()
#                 continue
#             stack.append(st[i])
#         return stack  
        
        
        
                