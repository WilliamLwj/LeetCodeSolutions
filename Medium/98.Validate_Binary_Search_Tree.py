
# Wrong idea: If left is BST, right is BST, then only need to compare left.val, root.val and right.val

# Idea: Use DFS to check the inorder values

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        minVal, maxVal = -2 ** 31 - 1, 2 ** 31
        return self.checkBST(root, minVal, maxVal)

    def checkBST(self, node, minVal, maxVal):
        if node == None:
            return True
        elif minVal < node.val < maxVal:
            return self.checkBST(node.left, minVal, node.val) and self.checkBST(node.right, node.val, maxVal)
        else:
            return False


# Idea: Use DFS to print the values out (Not necessary)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        InorderList = self.output(root, [])

        for i in range(len(InorderList) - 1):

            if InorderList[i + 1] <= InorderList[i]:
                return False

        return True

    def output(self, root, InorderList):

        if root is None:

            return InorderList

        else:

            InorderList = self.output(root.left, InorderList)
            InorderList.append(root.val)
            InorderList = self.output(root.right, InorderList)

            return InorderList