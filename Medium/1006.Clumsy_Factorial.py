
#Idea: edge cases

class Solution:
    def clumsy(self, n: int) -> int:

        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 6
        else:

            base = n * (n - 1) // (n - 2) + (n - 3)

            return (base - self.compute(n - 4))

    def compute(self, n):

        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 6
        else:

            return n * (n - 1) // (n - 2) - (n - 3) + self.compute(n - 4)