class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        ret = []
        Max = 0
        maxKey = 0
        for i in nums:
            myMap[i] = myMap.get(i, 0) + 1
        while k > 0:
            for key in myMap:
                if (myMap[key] > Max):
                    Max = myMap[key]
                    maxKey = key
            ret.append(maxKey)
            myMap[maxKey] = 0
            Max = 0
            k = k - 1
        return ret
