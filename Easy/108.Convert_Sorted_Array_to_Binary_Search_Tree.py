
#Idea: Simple Binary Split



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if len(nums) == 0:
            return None


        elif len(nums) == 1:

            return TreeNode(nums[0], left=None, right=None)

        else:

            split = len(nums) // 2

            return TreeNode(nums[split], left=self.sortedArrayToBST(nums[0:split]),
                            right=self.sortedArrayToBST(nums[split + 1: len(nums)]))




