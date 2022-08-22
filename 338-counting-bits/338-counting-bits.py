class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]  
        return dp  
    
    
        '''
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        '''
        # res = [0]
        # digit = 0
        # for i in range(1, n+1):
        #     while i != 0:
        #         digit += i % 2
        #         i //= 2
        #     res.append(digit)
        #     digit = 0
        # return res   