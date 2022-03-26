
# Idea: Better way of recursively writing BFS
class Solution:
    def compare(self, rootleft, rootright):
        if rootleft == None or rootright == None:
            return rootleft == rootright
        return rootleft.val == rootright.val and self.compare(rootleft.left, rootright.right) and self.compare(
            rootleft.right, rootright.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.compare(root.left, root.right)


# Idea: BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        root_list = [root]
        while len(root_list) > 0:

            for i in range(len(root_list) // 2):
                if root_list[i] is None and root_list[-1 - i] is None:
                    continue
                elif root_list[i] is not None and root_list[-1 - i] is not None:
                    if root_list[i].val != root_list[-1 - i].val:
                        return False
                else:
                    return False
            output = []
            for root in root_list:
                if root is not None:
                    output += [root.left, root.right]

            root_list = output
        return True




