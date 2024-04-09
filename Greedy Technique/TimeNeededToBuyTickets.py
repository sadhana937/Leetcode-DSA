class Solution1:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        for i, ticket in enumerate(tickets):
            if i <= k:
                # For anyone before or at k, they will be served either until they are done or until k is done
                count += min(tickets[k], ticket)
            else:
                # For those after k, they will be served one less time than k, unless they have fewer tickets than k
                count += min(tickets[k] - 1, ticket)
        return count


class Solution2:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        for i in range(len(tickets)):
            if i <= k:
                if tickets[k] > tickets[i]:
                    count += tickets[i]
                else:
                    count += tickets[k]
            else:
                if tickets[k] > tickets[i]:
                    count += tickets[i]
                else:
                    count += tickets[k] - 1

        return count
