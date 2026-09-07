class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        hand.sort()
        freqMap = Counter(hand)

        for num in hand:
            if freqMap[num]:
                for i in range(num, num + groupSize):
                    if not freqMap[i]:
                        return False
                    freqMap[i] -= 1
        return True