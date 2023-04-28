from collections import deque


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeStack = deque()
        reversedLinkedList = ListNode()
        firstReversedLinkedListNode = reversedLinkedList

        while head:
            nodeStack.append(head)
            head = head.next

        while len(nodeStack) > 0:
            reversedLinkedList.next = nodeStack.pop()
            reversedLinkedList.next.next = None

            reversedLinkedList = reversedLinkedList.next

        return firstReversedLinkedListNode.next
