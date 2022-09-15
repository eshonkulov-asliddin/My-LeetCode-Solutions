class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for idx, val in enumerate(prices):
            while stack and prices[stack[-1]] >= prices[idx]:
                prices[stack.pop()] -= prices[idx]
            stack.append(idx)
        return prices    
        
                
            
            