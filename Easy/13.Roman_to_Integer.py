
# Idea: Compute the whole thing backwards

class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        summ = 0
        temp = 0
        for i in range(1, len(s) + 1):
            if dictionary[s[-i]] >= temp:
                summ += dictionary[s[-i]]
            else:
                summ -= dictionary[s[-i]]
            temp = dictionary[s[-i]]

        return summ
