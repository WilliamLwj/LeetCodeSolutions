
# Idea: Use Counter, much faster for some reason

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        x = Counter(ransomNote)
        y = Counter(magazine)
        for i, v in x.items():
            if (x[i] <= y[i]):
                continue
            else:
                return False
        return True



# Idea: Use dictionary

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        dictionary = {}
        for letter in magazine:

            if letter in dictionary.keys():
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1

        for letter in ransomNote:

            if letter not in dictionary.keys():

                return False

            else:
                dictionary[letter] -= 1
                if dictionary[letter] < 0:
                    return False

        return True