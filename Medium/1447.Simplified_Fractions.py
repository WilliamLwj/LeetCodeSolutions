
# Idea: Use a set to record the fractions


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:

        values = set()
        return_list = []
        for i in range(1, n + 1):
            for j in range(1, i):
                val = j / i
                if val not in values:
                    values.add(val)
                    return_list.append(str(j) + '/' + str(i))

        return return_list