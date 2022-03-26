
# Idea: Use a queue

class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')' , '[':']' , '{':'}'}
        res = []
        for c in s:
            if c in dic:
                res.append(c)
            else:
                if (len(res) and dic[res[-1]]==c):
                    del res[-1]
                else:
                    return False
        return res == []