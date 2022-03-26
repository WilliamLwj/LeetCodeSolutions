
# Idea: Use carry


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1
        for i in range(len(digits)):

            new_digit = (digits[-i - 1] + carry) % 10
            carry = (digits[-i - 1] + carry) // 10
            digits[-i - 1] = new_digit
            if carry == 0:
                break

        if carry == 1:
            digits = [1] + digits

        return digits

