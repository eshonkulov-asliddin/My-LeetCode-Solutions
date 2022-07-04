class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
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
            