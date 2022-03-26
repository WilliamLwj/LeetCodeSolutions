
# Idea: Use carry again.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        if len(a) < len(b):
            temp = a
            a = b
            b = temp

        result = ""
        for i in range(len(b)):
            newresult = carry + int(a[-i - 1]) + int(b[-i - 1])
            result = str(newresult % 2) + result
            carry = newresult // 2

        for i in range(len(b), len(a)):
            newresult = carry + int(a[-i - 1])
            result = str(newresult % 2) + result
            carry = newresult // 2

        if carry == 1:
            result = "1" + result

        return result
