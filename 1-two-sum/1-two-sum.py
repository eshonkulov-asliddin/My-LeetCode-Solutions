class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Time Complexity: O(n2)
        Space Complexity: O(1)
        '''
        
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        
        # Hashmap
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        hashmap = dict()
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return [i, hashmap[nums[i]]]
            else:
                hashmap[target-nums[i]] = i
        