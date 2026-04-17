import re
class Solution:

    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(re.findall(r'[a-zA-Z0-9]', s)).lower()
        return cleaned==cleaned[::-1]