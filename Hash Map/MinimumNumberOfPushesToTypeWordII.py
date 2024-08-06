class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        push = 1
        output = 0
        key = 1
        count = sorted(count.values(), reverse = True)
        for value in count:
            if key == 9:
                push += 1
                key = 1
            output += push * value
            key += 1
        return output
