class Solution:
    def isValid(self, s: str) -> bool:
        
        '''
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        stack = []
        brackets = {
            ']': '[',
            ')': '(',
            '}': '{'
        }
        for char in s:
            if char not in brackets:
                stack.append(char)
                continue
                
            if not stack:
                return False
            last_opened = stack.pop()
            if last_opened != brackets[char]:
                return False

        return not stack
