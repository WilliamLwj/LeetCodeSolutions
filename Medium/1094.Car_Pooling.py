
# Idea: A much more clever way of expressing what I did

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        lst = []
        for n, start, end in trips:
            lst.append((start, n))
            lst.append((end, -n))
        lst.sort()
        pas = 0
        for loc in lst:
            pas += loc[1]
            if pas > capacity:
                return False
        return True








# Idea: Brute force, sort the time on board and the time off board (Still 50% better)

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        if len(trips) == 0:
            return True

        start_time = trips.copy()
        start_time.sort(key = lambda x: x[1])

        trips.sort(key = lambda x: x[2])

        passengers = 0
        end = trips[-1][-1] + 1
        for i in range(end):

            if len(start_time) > 0:
                while start_time[0][1] == i:
                    passengers += start_time[0][0]
                    start_time = start_time[1:]
                    if len(start_time) == 0:
                        break
            if len(trips) > 0:
                while trips[0][2] == i:
                    passengers -= trips[0][0]
                    trips = trips[1:]
                    if len(trips) == 0:
                        break
            if passengers > capacity:

                return False

        return True
