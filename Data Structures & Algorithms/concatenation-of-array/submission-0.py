class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new=nums[:]
        for i in nums :
            new.append(i)
        return new


        