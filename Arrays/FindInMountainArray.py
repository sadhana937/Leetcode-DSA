# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak_value = self.binarySearchPeak(mountain_arr)
        if peak_value == -1:
            return -1
        print(peak_value)
        left_result = self.binarySearch(mountain_arr, target, 0, peak_value, True)
        print(left_result)
        if left_result != -1:
            return left_result

        right_result = self.binarySearch(mountain_arr,target, peak_value + 1, mountain_arr.length() - 1, False)
        return right_result

    def binarySearchPeak(self, arr):
        low = 1
        high = arr.length() - 2
        while low < high:
            mid = low + (high - low) // 2
            if arr.get(mid) < arr.get(mid + 1):
                low = mid + 1
            else:
                high = mid - 1
        return low

    def binarySearch(self, arr, value, low, high, Increasing):
        while low <= high:
            mid = low + (high - low) // 2
            if arr.get(mid) == value:
                return mid
            elif (Increasing and arr.get(mid) < value) or (not Increasing and arr.get(mid) > value):
                low = mid + 1
            else:
                high = mid - 1
        return -1
