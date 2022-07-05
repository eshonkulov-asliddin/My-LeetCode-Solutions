class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """   
        
#         Time Complexity: O(log n)
#         Space Complexity: O(1) 
            
        # for i in range(len(s)//2):
        #     s[i], s[-1-i] = s[-1-i], s[i]
        
        
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        
        # l, r = 0, len(s)-1
        # while l < r:
        #     s[l], s[r] = s[r], s[l]
        #     l +=1
        #     r-=1
        
        # Recursion
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        def reverse(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                reverse(l+1, r-1)
        reverse(0, len(s)-1)                