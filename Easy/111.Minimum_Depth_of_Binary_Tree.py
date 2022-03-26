
#Idea: simply BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        nodes = [root]
        depth = 0
        while True:
            depth += 1
            new_nodes = []
            for node in nodes:
                if node.left is None and node.right is None:
                    new_nodes = None
                    break
                else:
                    if node.left is not None:
                        new_nodes.append(node.left)

                    if node.right is not None:
                        new_nodes.append(node.right)

            if new_nodes is None:
                break
            else:
                nodes = new_nodes

        return depth
