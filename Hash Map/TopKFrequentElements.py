class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key = lambda x: count[x])


class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        output = []
        count = dict(sorted(count.items(), key = lambda x: x[1], reverse = True)) 
        i       
        for key in count.keys():
            if k > 0:
                output.append(key)
                k -= 1
            else:
                return output
        return output

