from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(map(str, nums))
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
        str_nums.sort(key=cmp_to_key(compare))
        result = "".join(str_nums)
        return "0" if result[0] == "0" else result