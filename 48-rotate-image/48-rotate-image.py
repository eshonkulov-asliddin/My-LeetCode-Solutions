class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Time: O(m) where m is the number of cell
        Space: O(1)
        """
        
        l, r = 0, len(matrix) - 1
        
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                
                # save the top left i
                topLeft = matrix[top][l+i]
                
                # update top left with bottom left
                matrix[top][l+i] = matrix[bottom-i][l]
                
                #update bottom left with bottom right
                matrix[bottom - i][l] = matrix[bottom][r-i]
                
                #update bottom right with top right
                matrix[bottom][r-i] = matrix[top+i][r]
                
                # update top right with top left
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1
            
                