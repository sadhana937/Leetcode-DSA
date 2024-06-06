class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        hand.sort()

        for f in hand:
            if count[f] > 0:
                for i in range(groupSize):
                    if count[f + i] > 0:
                        count[f + i] -= 1
                    else:
                        return False
        return True
