
# Idea: recursive, not really BFS


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:

            bool1 = self.isSameTree(p.left, q.left)
            bool2 = self.isSameTree(p.right, q.right)

            boolvalue = bool1 and bool2 and p.val == q.val

            return boolvalue

