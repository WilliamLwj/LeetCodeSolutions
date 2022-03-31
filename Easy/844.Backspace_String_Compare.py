

#Idea: Start from the end. Although not really faster

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i = len(S) - 1
        j = len(T) - 1
        ci = 0
        cj = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    i -= 1
                    ci +=1
                elif ci > 0:
                    i -= 1
                    ci -= 1
                else:
                    break

            while j >= 0:
                if T[j] == "#":
                    j -= 1
                    cj +=1
                elif cj > 0:
                    j -= 1
                    cj -= 1
                else:
                    break

            if i < 0: return j < 0
            if j < 0: return i < 0
            if S[i] != T[j]: return False
            i -= 1
            j -= 1

        return True



# Idea: Just construct two lists

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        lists = []
        for i in range(len(s)):
            if s[i] == "#":
                if len(lists) > 0:
                    lists.pop()
            else:
                lists.append(s[i])

        listt = []
        for j in range(len(t)):
            if t[j] == "#":
                if len(listt) > 0:
                    listt.pop()
            else:
                listt.append(t[j])

        return lists == listt