
# Idea: Hashmap, edge cases

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        for i in range(len(time)):
            time[i] = time[i] % 60

        cnt = 0
        hashmap = {}
        for i in time:
            if i == 0:
                if 0 in hashmap.keys():
                    cnt = cnt + hashmap[0]
                    hashmap[0] += 1
                else:
                    hashmap[0] = 1
            else:
                if 60 - i in hashmap.keys():
                    cnt = cnt + hashmap[60 - i]

                if i in hashmap.keys():
                    hashmap[i] += 1
                else:
                    hashmap[i] = 1

        return cnt