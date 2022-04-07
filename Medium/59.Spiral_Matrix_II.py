
# Idea: Very Intuitive

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        matrix = []
        for i in range(n):
            row = [0] * n
            matrix.append(row)

        cnt = 0
        direct = 0
        pos = [0, -1]
        while cnt < n * n:
            d = directions[direct]
            pos[0] = pos[0] + d[0]
            pos[1] = pos[1] + d[1]
            cnt += 1
            matrix[pos[0]][pos[1]] = cnt

            if pos[0] + d[0] >= 0 and pos[0] + d[0] < n and pos[1] + d[1] >= 0 and pos[1] + d[1] < n:
                if matrix[pos[0] + d[0]][pos[1] + d[1]] != 0:
                    direct = direct + 1
            else:
                direct = direct + 1

            if direct >= 4:
                direct = 0

        return matrix