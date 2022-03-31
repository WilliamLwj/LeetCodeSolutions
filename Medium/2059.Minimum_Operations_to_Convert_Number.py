
# Idea: BFS(not really). Maintain a set of numbers already observed so we do not go back.


class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        seen = set()
        current = {start}

        turns = 0
        while len(seen) < 1001:
            # found in current turn
            if goal in current:
                return turns

            # go to next turn
            turns += 1
            nex = set()
            for x in current:
                for y in nums:
                    for cand in (x + y, x - y, x ^ y):
                        if cand == goal:
                            return turns
                        if 0 <= cand <= 1000:
                            if cand not in seen:
                                if cand not in current:
                                    nex.add(cand)

            # update
            seen |= current
            current = nex
            if not nex: break  # break infinite looping

        return -1