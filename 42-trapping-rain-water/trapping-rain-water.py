class Solution(object):

    def trap(self, height):

        n = len(height)

        if n <= 2:
            return 0

        left = 0
        right = n - 1

        leftMax = 0
        rightMax = 0

        water = 0

        while left < right:

            # Process smaller side
            if height[left] < height[right]:

                if height[left] >= leftMax:
                    leftMax = height[left]

                else:
                    water += leftMax - height[left]

                left += 1

            else:

                if height[right] >= rightMax:
                    rightMax = height[right]

                else:
                    water += rightMax - height[right]

                right -= 1

        return water