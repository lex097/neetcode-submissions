# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        iterate = l1
        factor = 1
        while iterate:
            num1 = num1 + (iterate.val*factor)
            factor = factor * 10
            iterate = iterate.next
        iterate = l2
        factor = 1
        while iterate:
            num2 = num2 + (iterate.val*factor)
            factor = factor * 10
            iterate = iterate.next
        add = num1 + num2
        mod = 10
        head = l1
        iterate = head
        while add != 0:
            iterate.val = add % 10
            add //= 10
            if (add > 0) and not iterate.next:
                iterate.next = ListNode(0, None)
            iterate = iterate.next
        iterate = None
        return head