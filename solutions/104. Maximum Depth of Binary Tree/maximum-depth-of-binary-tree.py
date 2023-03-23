# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        global max_level
        global curr_level
        max_level = 0
        curr_level = 0

        def walk(node: Optional[TreeNode]) -> None:
            global max_level
            global curr_level

            if node is None:
                return

            curr_level += 1
            walk(node.left)
            max_level = max(max_level, curr_level)
            curr_level -= 1

            curr_level += 1
            walk(node.right)
            max_level = max(max_level, curr_level)
            curr_level -= 1

        walk(root)
        return max_level
