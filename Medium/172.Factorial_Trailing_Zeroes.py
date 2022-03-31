
# Just add up the number divided by powers of 5

class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = n // 5
        cnt += n // 25
        cnt += n // 125
        cnt += n // 625
        cnt += n // 3125
        return cnt