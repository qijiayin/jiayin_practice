#11 container-with-most-water/
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2 :
            return 0
        n = len(height)
        maxVal = min(height[0], height[n-1]) * (n-1)
        beg = 0
        end = n - 1
        while(beg < end ):
            area = min(height[beg], height[end]) * (end - beg)
            maxVal = max(maxVal, area)
            if height[beg] > height[end]:
                end -= 1
            else:
                beg += 1
        return maxVal
