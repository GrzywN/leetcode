# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def walk(node: Optional[TreeNode], path: List[int]) -> List[int]:
            if node is None:
                return path

            walk(node.left, path)
            walk(node.right, path)

            path.append(node.val)
            return path

        return walk(root, [])
