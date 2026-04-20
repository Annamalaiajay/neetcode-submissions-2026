class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
           
            count[n] = count.get(n, 0) + 1
        
        
        ans = max(count, key=count.get)
        return ans