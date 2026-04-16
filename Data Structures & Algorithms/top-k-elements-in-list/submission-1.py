class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = {}
        new = []

        for num in nums:
            if num in ans:
                ans[num] += 1
            else:
                ans[num] = 1

        sor = sorted(ans.items(), key=lambda i: i[1], reverse=True)

        for key, count in sor:
            new.append(key)

        return new[:k]