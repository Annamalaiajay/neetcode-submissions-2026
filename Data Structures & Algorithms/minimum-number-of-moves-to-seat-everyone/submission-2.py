class Solution:
    def minMovesToSeat(self, seat: List[int], student: List[int]) -> int:
        seat.sort()
        student.sort()
        count=0
        for i in range(len(seat)):
            count+=abs(seat[i]-student[i])
        return count