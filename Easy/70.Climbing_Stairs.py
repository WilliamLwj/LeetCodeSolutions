
# Idea: Easiest dynamic programming

class Solution:
    def climbStairs(self, n: int) -> int:
        array = [[1] * (n + 1)][0]
        array[1] = 1

        for i in range(2, n + 1):
            array[i] = array[i - 1] + array[i - 2]

        return array[n]

