class Solution {
public:

    void nextPermutation(vector<int>& nums) {

        int n = nums.size();

        int index = -1;

        // Step 1:
        // Find first decreasing element from right
        for (int i = n - 2; i >= 0; i--) {

            if (nums[i] < nums[i + 1]) {
                index = i;
                break;
            }
        }

        // Step 2:
        // If breakpoint exists,
        // find next greater element from right
        if (index != -1) {

            for (int i = n - 1; i > index; i--) {

                if (nums[i] > nums[index]) {

                    swap(nums[i], nums[index]);
                    break;
                }
            }
        }

        // Step 3:
        // Reverse the remaining decreasing part
        reverse(nums.begin() + index + 1, nums.end());
    }
};