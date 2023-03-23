# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        def walk(node: 'Node', path: list[int]) -> list[int]:
            if node is None:
                return path

            path.append(node.val)
            for node in node.children:
                walk(node, path)

            return path

        return walk(root, [])
