class Solution:
    def mySqrt(self, x: int) -> int:
        x0 = 600
        a0 = (x - x0 * x0) / (2 * x0)
        
        for i in range(60):
            x0 = x0 + a0
            a0 = (x - x0 * x0) / (2 * x0)
            print(x0)
        return int(x0)