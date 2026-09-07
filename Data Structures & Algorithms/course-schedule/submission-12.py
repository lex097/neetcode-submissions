class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for i in prerequisites:
            preMap[i[0]].append(i[1])

        seen = set()
        self.finish = True
        def search(course):
            if course in seen:
                self.finish = False
                return
            seen.add(course)
            for crs in preMap[course]:
                search(crs)
            seen.remove(course)
            return

        for crs in prerequisites:
            search(crs[0])
        return self.finish
