
# Idea: Compute the distance and sort

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist = []
        for p in points:
            dist.append([p, sqrt(p[0] ** 2 + p[1] ** 2)])

        dist = sorted(dist, key=lambda x: x[1])

        output = []
        for i in range(k):
            output.append(dist[i][0])

        return output

