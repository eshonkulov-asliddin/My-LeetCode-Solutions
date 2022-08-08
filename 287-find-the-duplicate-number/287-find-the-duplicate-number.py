class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        '''
        Hashmap
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        '''
        
        d = dict()
        for i in nums:
            if i in d:
                return i
            else:
                d[i] = 1
                
        
        
        
        
        '''
        Brute Force
        Time Complexity: O(n2)
        Space Complexity: O(1)
        
        '''
        
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return nums[i]