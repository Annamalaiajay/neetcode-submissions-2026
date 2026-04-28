class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        text=s.split()
        if not text:
            return 0
        new=text[-1]
        return len(new)
        