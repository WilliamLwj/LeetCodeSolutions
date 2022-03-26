
#Idea: Greedy algorithm, just compute the numbers one by one

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

        num_rows = len(rowSum)
        num_cols = len(colSum)

        output = []
        for i in range(num_rows):
            rowi = []
            for j in range(num_cols):
                rowi.append(0)
            output.append(rowi)

        for i in range(num_rows):
            for j in range(num_cols):
                val = min(rowSum[i], colSum[j])

                rowSum[i] -= val
                colSum[j] -= val

                output[i][j] = val

        return output