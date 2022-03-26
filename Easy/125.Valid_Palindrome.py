

# Idea: Convert the string 

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-z0-9]",'',s.lower())
        return s == ''.join(reversed(s))