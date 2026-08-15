# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        curr = root
        self.max_diameter = 0
        # We're going to use dfs

        def dfs(node):
            if node == None:
                return 0

            left_side = dfs(node.left)
            right_side = dfs(node.right)

            self.max_diameter = max(self.max_diameter, left_side + right_side)
            return 1 + max(left_side, right_side)

        dfs(curr)

        return self.max_diameter