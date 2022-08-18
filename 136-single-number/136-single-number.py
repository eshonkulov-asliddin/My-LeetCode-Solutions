class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        '''
        Set
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        unique = set()
        
        for i in nums:
            if i not in unique:
                unique.add(i)
            
            else:
                unique.remove(i)   
        
        x = next(iter(unique))
        return x