# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #count nodes
        count = head
        nodes = 0
        while count:
            nodes = nodes + 1
            count = count.next
        nthnode = nodes - n # 0 indexed
        if nthnode == 0:
            return head.next
        currNode = 0
        iterNode = head
        while True:
            if currNode == nthnode - 1:
                iterNode.next = iterNode.next.next
                return head
            iterNode = iterNode.next
            currNode = currNode + 1
