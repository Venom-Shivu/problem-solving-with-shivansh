class Solution(object):

    def trap(self, height):

        left = 0
        right = len(height) - 1

        leftMax = 0
        rightMax = 0

        water = 0

        while left < right:

            hLeft = height[left]
            hRight = height[right]

            if hLeft < hRight:

                if hLeft > leftMax:
                    leftMax = hLeft
                else:
                    water += leftMax - hLeft

                left += 1

            else:

                if hRight > rightMax:
                    rightMax = hRight
                else:
                    water += rightMax - hRight

                right -= 1

        return water