# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            head = list1
            curr1 = curr1.next
        else:
            head = list2
            curr2 = curr2.next
        curr = head
        while (curr1 is not None) or (curr2 is not None):
            if not curr1:
                curr.next = curr2
                break
            elif not curr2:
                curr.next = curr1
                break
            elif curr1.val <= curr2.val:
                curr1next = curr1.next
                curr.next = curr1
                curr1 = curr1next
                curr = curr.next
            else:
                curr2next = curr2.next
                curr.next = curr2
                curr2 = curr2next
                curr = curr.next
        return head