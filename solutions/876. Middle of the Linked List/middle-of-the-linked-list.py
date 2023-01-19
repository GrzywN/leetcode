# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        listLength = 0
        currentNode = head
        
        while currentNode.next != None:
            currentNode = currentNode.next
            listLength += 1

        middleNodeIndex = ceil(listLength / 2)
        
        currentNode = head
        
        for _ in range(middleNodeIndex):
            currentNode = currentNode.next

        return currentNode
