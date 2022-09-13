class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        ROWS = COLS = len(matrix)
        colIdx = 0
        rowIdx = len(matrix) - 1
        oldmatrix = matrix
        res = []
        for row in range(ROWS):
            rowIdx = len(matrix) - 1
            cols = []
            for col in range(COLS):
                cols.append(matrix[rowIdx][colIdx])
                rowIdx -= 1
            res.append(cols)    
            colIdx += 1
            
        for i in range(len(matrix)):   
            matrix[i] = res[i]
