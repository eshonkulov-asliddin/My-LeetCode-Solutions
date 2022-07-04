class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Time Complexity: O(n)
        # Space Complexity: O(1) 
            
        # hashmap = {}
        # for i, k in enumerate(numbers):
        #     if k in hashmap:
        #         return [hashmap[k]+1, i+1]
        #     else:
        #         hashmap[target-k] = i
                
        
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        
        l, r = 0, len(numbers)-1
        
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1