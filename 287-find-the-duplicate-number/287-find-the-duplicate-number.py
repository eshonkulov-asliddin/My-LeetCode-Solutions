class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        '''
        Floyd's Algorithm
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        '''
        
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow 
        
        '''
        Hashmap
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        '''
        
#         d = dict()
#         for i in nums:
#             if i in d:
#                 return i
#             else:
#                 d[i] = 1
                
        
        
        
        
        '''
        Brute Force
        Time Complexity: O(n2)
        Space Complexity: O(1)
        
        '''
        
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return nums[i]