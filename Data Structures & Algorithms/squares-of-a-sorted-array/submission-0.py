class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            a=i*i
            ans.append(a)
        return sorted(ans)
        