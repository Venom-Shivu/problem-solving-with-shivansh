class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {

        vector<vector<int>> result;

        // Sorting helps in:
        // 1. Using two pointers
        // 2. Avoiding duplicate quadruplets
        sort(nums.begin(), nums.end());

        int n = nums.size();

        // First number
        for (int i = 0; i < n - 3; i++) {

            // Skip duplicate values for i
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            // Second number
            for (int j = i + 1; j < n - 2; j++) {

                // Skip duplicate values for j
                if (j > i + 1 && nums[j] == nums[j - 1]) {
                    continue;
                }

                // Two pointers for remaining two numbers
                int left = j + 1;
                int right = n - 1;

                while (left < right) {

                    // Use long long to avoid integer overflow
                    long long sum =
                        (long long)nums[i] +
                        nums[j] +
                        nums[left] +
                        nums[right];

                    // Valid quadruplet found
                    if (sum == target) {

                        result.push_back({
                            nums[i],
                            nums[j],
                            nums[left],
                            nums[right]
                        });

                        left++;
                        right--;

                        // Skip duplicate values
                        while (left < right &&
                               nums[left] == nums[left - 1]) {
                            left++;
                        }

                        while (left < right &&
                               nums[right] == nums[right + 1]) {
                            right--;
                        }
                    }

                    // Need larger sum
                    else if (sum < target) {
                        left++;
                    }

                    // Need smaller sum
                    else {
                        right--;
                    }
                }
            }
        }

        return result;
    }
};