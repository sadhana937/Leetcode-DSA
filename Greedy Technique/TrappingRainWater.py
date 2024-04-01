class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        i = 0
        j = len(height) - 1
        max_right_height = height[j]
        max_left_height = height[i]
        
        while i < j:
            if max_left_height < max_right_height:
                i += 1
                max_left_height = max(max_left_height, height[i])
                water += max_left_height - height[i]
            else:
                j -= 1
                max_right_height = max(max_right_height, height[j])
                water += max_right_height - height[j]

        return water

        
                
