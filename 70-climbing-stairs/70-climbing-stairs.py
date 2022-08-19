class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0: return 0 
        if n == 1: return 1
        if n == 2: return 2
        
        all_steps = 0
        two_step_before = 1
        one_step_before = 2
        for i in range(2, n):
            all_steps = one_step_before + two_step_before
            two_step_before = one_step_before
            one_step_before = all_steps
        return all_steps    