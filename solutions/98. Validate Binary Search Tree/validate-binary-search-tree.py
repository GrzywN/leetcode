# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def is_valid_bst(root: Optional[TreeNode], min_value=float('-inf'), max_value=float('inf')):
    if root is None:
        return True

    if root.val <= min_value or root.val >= max_value:
        return False

    return is_valid_bst(root.left, min_value, root.val) and is_valid_bst(root.right, root.val, max_value)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return is_valid_bst(root)
