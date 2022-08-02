class Solution:

        
#     def is_row_valid(self, board):
#         unique_row = set()
#         for i in range(len(board)):
#             for j in range(i, len(board)):
#                 if board[i][j] != '.' and board[i][j] in unique_row:
#                     return False
#                 else:
#                     unique_row.add(board[i][j])
                   
#             unique_row = set() 
            
#     def is_column_valid(self, board):
        
#         unique_col = set() 
        
#         for i in range(len(board)):
#             for j in range(len(board)):
#                 if board[j][i] != '.' and board[j][i] in unique_col:
#                     return False
#                 else:
#                     unique_col.add(board[j][i])
#             unique_col = set() 
            
#     def is_sub_box_valid(self, board):
#         squares = collections.defaultdict(set)
#         for i in range(9):
#             for j in range(9):
#                 if board[i][j] == '.':
#                     continue
#                 if board[i][j] in squares[(i //3, j // 3)]:
#                     return False
#                 squares[(i // 3, j // 3)].add(board[i][j])
                
        
            
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in cols[c] or board[r][c] in rows[r] or board[r][c] in squares[(r // 3, c // 3)]:
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True                
                

        # return (self.is_row_valid(board) and self.is_column_valid(board) and self.is_sub_box_valid(board))
            
        
        