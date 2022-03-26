
# Idea: Use string.split in Python



class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        lis=[]
        for i in s.split(' '):
            if i!=' ' and i!='':
                lis.append(i)
        if(len(lis)!=0):
            return len(lis[-1])
        else:
            return 0


# Idea: Two pointers

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        if len(s) == 0:
            return 0
        else:
            start = 0
            end = 0
            i = 0
            while (i < len(s)):
                if s[i]!= " ":
                    start = i
                    while s[i] != " " :
                        i = i + 1
                        if i >= len(s):
                            break
                    end = i - 1
                else:
                    i = i + 1

            return end - start + 1