class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        '''
        Two Pointer
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        max_water = 0
        l, r = 0, len(height)-1
        while l <= r:
            distance = r - l
            vertical_line = min(height[l], height[r])
            
            area = distance * vertical_line
            max_water = max(area, max_water)
            if height[l] < height[r]:
                l += 1
                
            else:
                r -= 1
        return max_water                
        
        
        '''
        Brute Force
        Time Complexity: O(n2)
        Space Complexity: O(1)
        
        '''
#         max_water = 0
        
#         for i in range(len(height)-1):
#             for j in range(i+1, len(height)):
#                 distance = j - i
#                 vertical_line = min(height[i], height[j])
                
#                 area = distance * vertical_line
                
#                 max_water = max(max_water, area)
#         return max_water                