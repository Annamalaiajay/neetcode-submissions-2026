class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        result_num = num + 1
        result_list = [int(d) for d in str(result_num)]
        return result_list
        