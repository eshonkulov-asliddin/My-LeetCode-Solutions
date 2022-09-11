class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        
       [ [2,1,2,0],
         [3,4,5,2],
         [1,3,1,5] ]
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
             
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

                        
#         rows = defaultdict(list)
#         cols = defaultdict(list)

#         row_num = 0
#         col_num = 0
#         for row in matrix:
#             for col in row:
#                 if col == 0:
#                     rows[row_num] = [0] * len(row)
#                     cols[col_num] = 0
#                 col_num += 1
#             row_num += 1
#             col_num = 0

#         i, j = 0 ,0 
#         for row in matrix:
#             if i in rows:
#                 matrix[i] = rows[i]
#                 i += 1
#             else:    
#                 for col in row:
#                     if j in cols:
#                         matrix[i][j] = 0
#                     j += 1    
#                 i += 1
#                 j = 0
#         return matrix    

