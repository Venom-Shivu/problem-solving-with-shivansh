class Solution {
public:
    
    int removeElement(vector<int>& nums, int val) {

        // k will store the position
        // where next valid element should go
        int k = 0;

        // Traverse entire array
        for (int i = 0; i < nums.size(); i++) {

            // Keep only elements not equal to val
            if (nums[i] != val) {

                nums[k] = nums[i];
                k++;
            }
        }

        // Number of remaining elements
        return k;
    }
};