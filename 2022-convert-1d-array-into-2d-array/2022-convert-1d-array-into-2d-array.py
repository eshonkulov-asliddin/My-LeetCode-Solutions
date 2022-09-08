class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        res = []
        if m * n < len(original) or m*n > len(original):
            return []
        #aproach2
        res = []
        for i in range(0, n*m, n):
            res.append(original[i:i+n])
        return res
        #Aproach1 
        # newArr = []
        # i = 0
        # for row in range(m):
        #     colm = []
        #     for col in range(n):
        #         colm.append(original[i])
        #         i += 1
        #     newArr.append(colm) 
        # return newArr    
         