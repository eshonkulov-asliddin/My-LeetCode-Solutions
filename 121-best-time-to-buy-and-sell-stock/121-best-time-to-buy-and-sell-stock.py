class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        '''
        Two Pointer
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        n = len(prices)
        l, r = 0, 1
        
        max_profit = 0
        while r < n:
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:    
                l = r
            r += 1

        return max_profit    
               
        '''
        Brute Force
        Time Complexity: O(n2)
        Space Comlexity: O(1)
        
        '''
        
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         max_profit = max(max_profit, profit)
        # return max_profit                