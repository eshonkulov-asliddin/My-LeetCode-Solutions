class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    
        l, r = 0 ,len(letters)-1
        
        if letters[l] > target or letters[r] <= target:
            return letters[0]
        
        while l < r:
            mid = (l+r) // 2
            if letters[mid] > target:
                r = mid 
            else:
                l = mid + 1
                
        return letters[l]        
        
        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        
        # for char in letters:
        #     if char > target:
        #         return char
        # return letters[0]