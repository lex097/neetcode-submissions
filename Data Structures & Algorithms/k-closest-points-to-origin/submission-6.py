class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceMap = {}
        for point in points:
            if point[0]**2 + point[1]**2 not in distanceMap:
                distanceMap[point[0]**2 + point[1]**2] = []
            distanceMap[point[0]**2 + point[1]**2].append(point)
        maxHeap = []
        for distance in distanceMap.keys():
            for i in range(len(distanceMap[distance])):
                heapq.heappush(maxHeap, -distance)
            while len(maxHeap) > k:
                heapq.heappop(maxHeap)
        ret = []
        for distance in maxHeap:
            ret.append(distanceMap[-distance][-1])
            distanceMap[-distance].pop()
        
        return ret