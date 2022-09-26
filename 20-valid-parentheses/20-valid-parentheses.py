class Solution:
    def isValid(self, s: str) -> bool:
        
        '''
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        stack = []
        
        brackets = {
            ")": '(',
            "]": "[",
            "}": "{"
        }
        
        for i in s:
            if i not in brackets:
                stack.append(i)
                continue
                
            if not stack: return False
            
            cur = stack.pop()
            if cur != brackets[i]:
                return False
                
        return len(stack) == 0       