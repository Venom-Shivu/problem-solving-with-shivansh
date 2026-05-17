class Solution {
public:

    int searchInsert(vector<int>& nums, int target) {

        int left = 0;
        int right = nums.size() - 1;

        while (left <= right) {

            int mid = left + (right - left) / 2;

            // Target found
            if (nums[mid] == target) {
                return mid;
            }

            // Search right half
            else if (nums[mid] < target) {
                left = mid + 1;
            }

            // Search left half
            else {
                right = mid - 1;
            }
        }

        // Correct insertion position
        return left;
    }
};