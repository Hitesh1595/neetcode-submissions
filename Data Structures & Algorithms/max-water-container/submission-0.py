class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) -1
        max_water = 0

        while left < right:
            width = right - left
            ht = min(heights[left],heights[right])
            max_water = max(max_water,width * ht)
            if heights[left] <= ht:
                left += 1
            else:
                right -= 1
        return max_water

