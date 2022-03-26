
# Idea: LCP of all the strings is a CP of any two strings

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        s = ""
        for a in zip(*strs):
            if len(set(a)) == 1:
                s += a[0]
            else:
                break
        return s