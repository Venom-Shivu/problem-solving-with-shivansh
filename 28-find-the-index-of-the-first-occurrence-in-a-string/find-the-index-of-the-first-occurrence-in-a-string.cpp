class Solution {
public:
    
    int strStr(string haystack, string needle) {

        int n = haystack.size();
        int m = needle.size();

        // Try every possible starting position
        for (int i = 0; i <= n - m; i++) {

            int j = 0;

            // Compare characters one by one
            while (j < m && haystack[i + j] == needle[j]) {
                j++;
            }

            // Entire needle matched
            if (j == m) {
                return i;
            }
        }

        // No match found
        return -1;
    }
};