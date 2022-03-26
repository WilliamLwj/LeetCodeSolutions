
# Idea: Two pointers. For python, we can just use remove()


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i] # or nums.remove[nums[i]]
            else:
                i += 1
        return len(nums)