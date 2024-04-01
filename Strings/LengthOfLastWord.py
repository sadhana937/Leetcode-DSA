class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        words = [word for word in s.split(" ") if word]
        return len(words[-1]) if words else 0

class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        s = s.rstrip()
        for i in s[::-1]:
            if i == " ":
                break
            count += 1
        return count
