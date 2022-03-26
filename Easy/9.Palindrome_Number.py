
# Idea: See if the lower half matches the upper half

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            num = list(str(x))
            length = len(num)
            if length < 3:
                return num == num[::-1]
            elif length % 2 == 0:
                index = int(length/2)
                return num[:index:1] == num[:(index - 1):-1]
            elif length % 2 != 0:
                index = int((length / 2) + 1)
                print(num[:(index - 2):-1])
                return num[:index:1] == num[:(index - 2):-1]