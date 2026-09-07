#global time, #follower map, #post map
class Twitter:

    def __init__(self):
        self.time = 0
        self.followerMap = {} #user -> users
        self.postMap = {} #user -> posts

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.postMap:
            self.postMap[userId] = []
        self.postMap[userId].append([self.time, tweetId])
        self.time = self.time + 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        ret = []
        if userId not in self.followerMap:
            self.followerMap[userId] = set()
        self.followerMap[userId].add(userId)
        for following in self.followerMap[userId]:
            if following not in self.postMap:
                continue
            for post in self.postMap[following]:
                heapq.heappush(heap, post)
                if len(heap) > 10:
                    heapq.heappop(heap)
        for i in range(len(heap)):
            post = heapq.heappop(heap)
            post = post[1]
            ret.append(post)
        ret.reverse()
        return ret
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followerMap:
            self.followerMap[followerId] = set()
        self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followerMap[followerId]:
            return
        self.followerMap[followerId].remove(followeeId)