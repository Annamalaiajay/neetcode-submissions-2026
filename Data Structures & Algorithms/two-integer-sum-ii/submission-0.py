class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pt1 = 0
        pt2 = len(numbers) - 1

        while pt1 < pt2:
            curr = numbers[pt1] + numbers[pt2]

            if curr == target:
                return [pt1 + 1, pt2 + 1]   
            elif curr > target:
                pt2 -= 1
            else:
                pt1 += 1