class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        current = 0
        for num in nums:
            if num == 1:
                current += 1
                if current > ones:
                    ones = current
            else:
                current = 0 
                
        return ones