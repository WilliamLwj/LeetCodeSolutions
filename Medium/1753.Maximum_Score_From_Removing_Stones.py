

# Idea: Use a heap. It is always safe to draw from the top 2

import heapq


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # -ive sign because there is no max-heap in python
        l = [-a, -b, -c]

        # to convert it into heap
        heapq.heapify(l)

        ans = 0
        while l.count(0) < 2:
            x = heapq.heappop(l)
            y = heapq.heappop(l)
            heapq.heappush(l, x + 1)
            heapq.heappush(l, y + 1)
            ans += 1
        return ans


# Idea: I don't really understand


class Solution:
    def maximumScore(self, a, b, c):
        ans = 0

        x, y, z = sorted((a, b, c))

        while x > 0 and y > 0 and x + y > z:
            x -= 1
            y -= 1
            ans += 1
        ans += x + y

        return ans