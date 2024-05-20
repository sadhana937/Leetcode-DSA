class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def recursion(index, summ):
            if index == len(nums):
                return summ
            include = recursion(index + 1, summ ^ nums[index])
            exclude = recursion(index + 1, summ)
            
            return include + exclude
        
        return recursion(0, 0)
