
#Idea: BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        node_list = [root]
        depth = 0

        while len(node_list) > 0:
            new_nodes = []
            for node in node_list:
                if node is not None:
                    new_nodes += [node.left, node.right]

            if len(new_nodes) > 0:
                depth += 1
            node_list = new_nodes
        return depth