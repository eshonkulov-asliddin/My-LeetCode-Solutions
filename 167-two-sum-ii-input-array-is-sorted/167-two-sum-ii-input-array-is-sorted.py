class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Two Pointer
        Time Complexiy: O(n)
        Space Complexity: O(1)
        
        '''
        
        r = len(numbers)-1
        index_r = len(numbers)
        
        for l in range(len(numbers)):
            if numbers[l] + numbers[r] == target:
                return [l+1, index_r]
            elif numbers[l] + numbers[r] > target:
                index_r -= 1
            
            elif numbers[l] + numbers[r] < target:
                continue
        
        '''
        Hashmap
        Time Complexiy: O(n)
        Space Complexity: O(n)
        
        '''
#         d = dict()
        
#         for i, k in enumerate(numbers):
#             if k in d:
#                 return [d[k], i+1]
#             d[target-k] = i+1
                
        
        '''
        Brute Force
        Time Complexiy: O(N2)
        Space Complexity: O(1)
        
        '''
        
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Brute Force 
        # Time Complexity: O(n2)
        # Space Comlexity: O(1)
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i]+numbers[j] == target:
        #             return [i+1, j+1]
        #         elif numbers[i]+numbers[j] > target:
        #             continue
        
        
        
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        
        l, r = 0, len(numbers)-1
        
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum == target:
                return [l+1, r+1]
            elif curSum > target:
                r -= 1
            else:
                l += 1

        # Time Complexity: O(n)
        # Space Complexity: O(1) 
            
#         hashmap = {}
#         for i, k in enumerate(numbers):
#             if k in hashmap:
#                 return [hashmap[k]+1, i+1]
#             else:
#                 hashmap[target-k] = i
            