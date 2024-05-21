class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        def backtracking(index, subset):
            output.append(subset[:])

            for i in range(index, len(nums)):

                subset.append(nums[i])

                backtracking(i + 1, subset)

                subset.pop()

        backtracking(0, [])
        return output

class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        def backtracking(index, subset):
            if index >= len(nums):
                return output.append(subset[:])
            subset.append(nums[index])
            backtracking(index + 1, subset)
            subset.remove(nums[index])
            backtracking(index + 1, subset)

        backtracking(0, [])
        return output
