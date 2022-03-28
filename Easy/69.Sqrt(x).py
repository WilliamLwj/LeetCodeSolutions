
# Idea: Binary Search

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2
            curr = mid * mid
            if curr <= x and ((mid + 1) * (mid + 1)) > x:
                return int(mid)

            if curr > x:
                right = mid - 1
            else:
                left = mid + 1