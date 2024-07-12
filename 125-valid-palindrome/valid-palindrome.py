import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        def remove_non_alpha_numeric_char(s: str) -> str:
            return re.sub(r"[^a-zA-Z0-9]", "", s).lower()

        s = remove_non_alpha_numeric_char(s)
        x = 0
        y = len(s) - 1

        while x <y:
            if s[x]!=s[y]:
                return False
            else:
                x+=1
                y-=1
        return True