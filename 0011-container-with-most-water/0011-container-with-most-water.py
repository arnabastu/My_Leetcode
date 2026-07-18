class Solution(object):
    def maxArea(self, height):
        n = len(height)
        l = 0
        r = n -1
        area_max = 0
        while l < r:
            area = min(height[l],height[r]) * (r-l)
            area_max = max(area_max , area)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return area_max