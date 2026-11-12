class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-i for i in nums]
        heapq.heapify(heap)
        ret = 0
        for i in range(k):
            ret = heapq.heappop(heap)
        return -ret



