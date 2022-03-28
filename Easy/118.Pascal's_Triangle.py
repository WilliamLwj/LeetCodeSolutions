
# Idea: Use recursion

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            output = [[1], [1, 1]]
            for i in range(2, numRows):
                list1 = [1]
                for j in range(0, i - 1):
                    list1.append(output[i - 1][j] + output[i - 1][j + 1])

                list1.append(1)

                output.append(list1)

            return output