class Solution:
    def plusOne(self, digits: List[int], index=-1) -> List[int]:
        digits[index] += 1
        
        
        if digits[index] == 10:
            digits[index] = 0
            try:
                self.plusOne(digits, index -1)
            except:
                digits.insert(0, 1)
        return digits    
               