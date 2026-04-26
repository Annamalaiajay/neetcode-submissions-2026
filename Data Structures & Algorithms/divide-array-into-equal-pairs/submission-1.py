class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums)%2!=0:
            return False
        count={}
        for n in nums:
            count[n]=count.get(n,0)+1
        for num, value in count.items():
            if value%2!=0:
                return False
        return True
        