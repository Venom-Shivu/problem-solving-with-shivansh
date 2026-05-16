class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        # Binary search should be applied on smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x = len(nums1)
        y = len(nums2)

        low = 0
        high = x

        while low <= high:

            # Partition position for nums1
            partitionX = (low + high) // 2

            # Partition position for nums2
            partitionY = (x + y + 1) // 2 - partitionX

            # Elements around partition in nums1
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            # Elements around partition in nums2
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            # Valid partition found
            if maxLeftX <= minRightY and maxLeftY <= minRightX:

                # If total elements are odd
                if (x + y) % 2:
                    return float(max(maxLeftX, maxLeftY))

                # If total elements are even
                return (
                    max(maxLeftX, maxLeftY) +
                    min(minRightX, minRightY)
                ) / 2

            # Move search toward left
            elif maxLeftX > minRightY:
                high = partitionX - 1

            # Move search toward right
            else:
                low = partitionX + 1