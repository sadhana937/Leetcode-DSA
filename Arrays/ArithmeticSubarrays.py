'''
# This algorithm doesn't work if the elements are not in AP but their sum is equal to n*(a+l)/2
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for x in range(len(l)):
            temp = nums[l[x] : r[x] + 1]
            temp.sort()
            n = len(temp)
            sum_of_ap = (n * (temp[0] + temp[n - 1])) / 2 
            if abs(sum(temp) - sum_of_ap) < 1e-9:
                result.append(True)
            else:
                result.append(False)
        return result
'''
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for x in range(len(l)):
            temp = nums[l[x] : r[x] + 1]
            temp.sort()
            diff = temp[1] - temp[0]
            flag = 0
            for i in range(1, len(temp)):
                if (temp[i] - temp[i - 1]) != diff:
                    result.append(False)
                    flag = 1
                    break
            if flag == 0:
                result.append(True)
        return result
