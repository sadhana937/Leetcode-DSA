# Space complexity: O(1)
class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        left_product = 1
        for i in range(n):
            output[i] *= left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        
        return output

# Space complexity: O(n)
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = 1
        output = []

        postfix_prod = [1] * (n + 1)
        postfix_prod[n - 1] = nums[n - 1]

        for i in range(n - 1, -1, -1):
            postfix_prod[i] = postfix_prod[i + 1] * nums[i]

        output.append(postfix_prod[1])

        for i in range(1, n):
            left_prod *= nums[i - 1]
            output.append(left_prod * postfix_prod[i + 1])
        
        return output
