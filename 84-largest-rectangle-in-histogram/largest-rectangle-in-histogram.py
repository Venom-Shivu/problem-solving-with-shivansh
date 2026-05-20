class Solution:
    def largestRectangleArea(self, heights):
        stack = []  # stores indices
        max_area = 0
        
        heights.append(0)  # force processing of all bars
        
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                
                # width calculation
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                
                max_area = max(max_area, h * width)
            
            stack.append(i)
        
        return max_area