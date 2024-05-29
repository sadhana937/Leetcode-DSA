class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diff = [0] * len(s)
        for i in range(len(s)):
            diff[i] = abs(ord(s[i]) - ord(t[i]))

        left = 0
        cur_cost = 0
        max_count = 0

        for right in range(len(diff)):
            cur_cost += diff[right]

            while cur_cost > maxCost:
                cur_cost -= diff[left]
                left += 1

            max_count = max(max_count, right - left + 1)
        return max_count
