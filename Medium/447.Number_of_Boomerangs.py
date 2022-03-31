
# Idea: Use distance to construct a hashmap

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:

        if len(points) < 3:
            return 0
        else:
            dist_array = []
            for i in range(len(points)):
                dist = {}
                for j in range(len(points)):
                    if j == i:
                        continue
                    distance = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                    if distance in dist.keys():
                        dist[distance].append(j)
                    else:
                        dist[distance] = [j]
                dist_array.append(dist)
            cnt = 0
            for i in range(len(points)):
                for distance in dist_array[i].keys():
                    if len(dist_array[i][distance]) >= 2:
                        cnt = cnt + len(dist_array[i][distance]) * (len(dist_array[i][distance]) - 1)

            return cnt


