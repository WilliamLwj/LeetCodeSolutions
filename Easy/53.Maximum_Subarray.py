# Idea: If negative, it is always better to not include it.




class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # meh = max ending here & msf = max so far
        meh = 0
        msf = nums[0]

        for i in nums:

            # Add every element to meh
            meh += i

            # Replace if greater than msf
            if (meh > msf):
                msf = meh

                # If negative make meh = 0
            if (meh < 0):
                meh = 0

        return msf