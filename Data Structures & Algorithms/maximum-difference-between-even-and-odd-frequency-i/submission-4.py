class Solution:
    def maxDifference(self, s: str) -> int:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        odd = -1
        even = float('inf')
        for f in count.values():
            if f % 2 != 0: 
                odd = max(odd, f)
            else:       
                even = min(even, f)
        return odd - even