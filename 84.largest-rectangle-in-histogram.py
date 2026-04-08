class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        best = 0
        n = len(heights)
        stack = []
        for i in range(n):
            height = heights[i]
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i-left-1
                area = h*width
                best = max(area, best)

            stack.append(i)

        while stack:
            h = heights[stack.pop()]
            left = stack[-1] if stack else -1
            width = n - left - 1
            best = max(best, h * width)
        return best
        