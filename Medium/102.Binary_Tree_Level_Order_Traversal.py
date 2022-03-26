

# Idea: BFS


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []
        else:

            value_list = []
            nodes = [root]
            while len(nodes) > 0:
                values = []
                new_nodes = []
                for node in nodes:
                    if node is not None:
                        values.append(node.val)
                        new_nodes += [node.left, node.right]
                if len(values) > 0:
                    value_list.append(values)
                nodes = new_nodes

            return value_list