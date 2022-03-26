
# Idea: straightforward, but a better algo exists
# TODO: Implement KMP


class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)




class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        else:
            needle_length = len(needle)

            for i in range(len(haystack)):
                if haystack[i] == needle[0]:
                    if i + needle_length <= len(haystack):
                        if haystack[i: i + needle_length] == needle:
                            return i

            return -1