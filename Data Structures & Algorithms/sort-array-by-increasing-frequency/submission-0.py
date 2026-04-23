class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
        nums.sort(key=lambda x: (count[x], -x))
        return nums
        