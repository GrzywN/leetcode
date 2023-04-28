# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeAndNext = dict()

        while head:
            nodeAndNext[head] = head.next

            if head.next in nodeAndNext:
                return nodeAndNext[head]

            head = head.next

        return None
