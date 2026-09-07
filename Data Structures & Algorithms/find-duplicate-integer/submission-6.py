#think of your array as a linked list
#the node that you are pointing at is the index
#the value of that index is what you are pointing at next
#once you find the "cycle", start a pointer at the beginning
#incremeent both one by one, then you have the "start" of your cycle


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow