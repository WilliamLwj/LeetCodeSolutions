
#Idea: Hard. Greedy and sort of dynamic programming. The main idea is to go from the end to the front, if at any point,
# it can directly jump to the end, then it must be able to jump to point that can jump to the end, that have
# indices larger than itself.


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        minn = 1

        # From the second last, -1 and -1, until reach 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= minn:
                reach = True
            else:
                reach = False
            if reach:
                minn = 1
            else:
                minn += 1

        return reach