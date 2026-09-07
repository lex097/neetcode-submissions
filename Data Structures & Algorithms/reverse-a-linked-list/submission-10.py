# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(first, prev):
            if not first:
                return prev
            nextNode = first.next
            first.next = prev
            return reverse(nextNode, first)
        return reverse(head, None)