#while + for loop, while loop updates heap, for loop pops from heap
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        cycles = 0
        q = deque()
        while maxHeap or q:
            cycles += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, cycles + n])
            if q and q[0][1] == cycles:
                heapq.heappush(maxHeap, q.popleft()[0])
        return cycles