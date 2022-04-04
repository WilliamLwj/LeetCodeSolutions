
#Idea: Basic Dynamic Programming

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            maximum = 1
            array = [0, 1]
            for i in range(2, n + 1):
                if (i % 2 == 0):
                    num = array[i // 2]
                else:
                    num = array[(i - 1) // 2] + array[(i + 1) // 2]

                if num >= maximum:
                    maximum = num

                array.append(num)

        return maximum
