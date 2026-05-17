class Solution {
public:
    
    int removeDuplicates(vector<int>& nums) {

        // If array has only one element
        // it's already unique
        if (nums.size() == 1)
            return 1;

        // uniqueIndex points to the last unique element
        int uniqueIndex = 0;

        // Start checking from second element
        for (int i = 1; i < nums.size(); i++) {

            // Found a new unique element
            if (nums[i] != nums[uniqueIndex]) {

                uniqueIndex++;

                // Place unique element at correct position
                nums[uniqueIndex] = nums[i];
            }
        }

        // Number of unique elements
        return uniqueIndex + 1;
    }
};