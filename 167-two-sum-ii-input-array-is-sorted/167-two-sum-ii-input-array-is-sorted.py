class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i, k in enumerate(numbers):
            if k in hashmap:
                return [hashmap[k]+1, i+1]
            else:
                hashmap[target-k] = i
                
                