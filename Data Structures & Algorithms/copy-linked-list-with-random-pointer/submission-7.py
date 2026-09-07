"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #copy linkedlist
        dummy = Node(1)
        last = dummy
        iterate = head

        while iterate:
            last.next = Node(iterate.val, iterate.next, None)
            iterate = iterate.next
            last = last.next
        copyHead = dummy.next
        #map indices
        iterate = copyHead
        iterate2 = head
        index = 0
        copyNodeMap = {}
        nodeToIndex = {}
        while iterate:
            copyNodeMap[index] = iterate
            nodeToIndex[iterate2] = index
            iterate = iterate.next
            iterate2 = iterate2.next
            index = index + 1
            

        #set node.random
        iterate1 = copyHead
        iterate2 = head
        while iterate1:
            if iterate2.random is None:
                iterate1.random = None
            else:
                iterate1.random = copyNodeMap[nodeToIndex[iterate2.random]]
            iterate1 = iterate1.next
            iterate2 = iterate2.next
        return copyHead

