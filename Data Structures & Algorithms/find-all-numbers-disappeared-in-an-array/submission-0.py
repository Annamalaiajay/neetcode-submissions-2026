class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nu=set(nums)
        new=[]
        for i in range(1,len(nums)+1):
            if i not in nu:
                new.append(i)
        return new