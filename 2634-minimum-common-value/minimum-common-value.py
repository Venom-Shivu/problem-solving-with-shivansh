class Solution:
    def getCommon(self, nums1, nums2):

        i = j = 0
        n1 = len(nums1)
        n2 = len(nums2)

        while i < n1 and j < n2:

            a = nums1[i]
            b = nums2[j]

            if a == b:
                return a

            if a < b:
                i += 1
            else:
                j += 1

        return -1