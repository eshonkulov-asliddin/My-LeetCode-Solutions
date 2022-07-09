class Solution:
    
    # Time Complexity: O(m*n)
    # Space Complexity: O(1)
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_pixel = image[sr][sc]
        self.dfs(image, sr, sc, color, starting_pixel)
        
        return image
        
        
    def dfs(self, image, sr, sc, color, starting_pixel):
        if sr < 0 or sr > len(image) - 1 or sc < 0 or sc > len(image[0])-1 or image[sr][sc] == color or image[sr][sc] != starting_pixel:
            return
        
        image[sr][sc] = color
        
        self.dfs(image, sr+1, sc, color, starting_pixel)
        self.dfs(image, sr-1, sc, color, starting_pixel)
        self.dfs(image, sr, sc+1, color, starting_pixel)
        self.dfs(image, sr, sc-1, color, starting_pixel)
        