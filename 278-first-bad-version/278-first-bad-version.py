# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
## Binary Search   
## Time Complexity : O(log n)
        low = 0
        high = n
        ans = 0
        
        while low <= high:
            mid = (high + low) // 2
            is_bad = isBadVersion(mid)
            if is_bad:
                ans = mid
                high = mid -1
            else:
                low = mid + 1
                
        return ans                
            
            
    
## Linear Search
## Time Complexity: O(n)
## Space Complexity: O(1)

#             i = 0
#             while i <= n:
#                 is_bad = isBadVersion(i)
#                 if is_bad:
#                     return i
#                 i+= 1
                