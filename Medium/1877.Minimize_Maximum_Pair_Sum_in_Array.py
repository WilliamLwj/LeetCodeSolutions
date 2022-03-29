

#Idea: Quite intuitive, just sort it


class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        maximum_sum = 0

        nums.sort()

        for i in range(len(nums) // 2):

            if nums[i] + nums[-i - 1] > maximum_sum:
                maximum_sum = nums[i] + nums[-i - 1]

        return maximum_sum