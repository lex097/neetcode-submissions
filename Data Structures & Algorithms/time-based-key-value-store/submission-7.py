# { key : [[timestamp, value]] } map[key] - > [[], [], []] -> 


class TimeMap:

    def __init__(self):
        self.myMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.myMap[key].append([timestamp, value])
    def get(self, key: str, timestamp: int) -> str: #binary search timestamp or closest timestamp LESS than timestamp
        myList = self.myMap[key]
        l, r = 0, len(myList) - 1
        retIndex = float ('inf')
        while r >= l:
            m = (r + l) // 2
            if myList[m][0] <= timestamp:
                retIndex = m
                l = m + 1
            else:
                r = m -1
        if retIndex == (float ('inf')):
            return ""
        return myList[retIndex][1]