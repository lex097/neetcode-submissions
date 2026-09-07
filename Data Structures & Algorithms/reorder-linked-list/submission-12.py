# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # split list into 2
        f = head.next
        s = head
        while f and f.next:
            f = f.next.next
            s = s.next
        back = s.next
        front = head
        s.next = None

        # reverse 2nd list
        prev = None
        while back:
            nxt = back.next
            back.next = prev
            prev = back
            back = nxt
        back = prev
        # merge lists
        currFront = front
        currBack = back
        curr = head
        while currBack:
            tmp1 = currFront.next
            tmp2 = currBack.next
            currFront.next = currBack
            currBack.next = tmp1
            currFront = tmp1
            currBack = tmp2