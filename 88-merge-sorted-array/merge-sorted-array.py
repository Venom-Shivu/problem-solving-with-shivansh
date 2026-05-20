class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Initialize three pointers
        p1 = m - 1       # End of valid elements in nums1
        p2 = n - 1       # End of nums2
        p = m + n - 1    # Actual end of nums1 array
        
        # While there are elements in both arrays to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If nums2 still has elements (e.g., nums1 was exhausted first)
        # We copy the remaining elements from nums2 into the front of nums1
        # If nums1 still has elements, they are already in the correct position
        nums1[:p2 + 1] = nums2[:p2 + 1]