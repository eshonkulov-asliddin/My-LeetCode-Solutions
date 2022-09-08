class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        if m * n < len(original) or m*n > len(original):
            return []
        
        newArr = []
        i = 0
        for row in range(m):
            colm = []
            for col in range(n):
                colm.append(original[i])
                i += 1
            newArr.append(colm) 
        return newArr    
         