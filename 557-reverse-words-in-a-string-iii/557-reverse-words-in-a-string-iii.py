class Solution:
    def reverseWords(self, s: str) -> str:
        
#         Time Complexity: O(n)
#         Space Complexity: O(n)   
            
#         s_list = s.split()
#         for i in range(len(s_list)):
#             s_list[i] = s_list[i][::-1]
        
#         ans = " ".join(s_list)
#         return ans
        
    
        # One line of code
        # Idea same with the code above
        return ' '.join(i[::-1] for i in s.split())