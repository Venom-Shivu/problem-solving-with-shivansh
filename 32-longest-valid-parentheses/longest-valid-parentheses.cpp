class Solution {
public:

    int longestValidParentheses(string s) {

        stack<int> st;

        // Base index before valid substring starts
        st.push(-1);

        int maxLength = 0;

        for (int i = 0; i < s.size(); i++) {

            // Opening bracket
            if (s[i] == '(') {

                st.push(i);
            }

            else {

                // Match one opening bracket
                st.pop();

                // No matching opening bracket exists
                if (st.empty()) {

                    // Set new boundary
                    st.push(i);
                }

                else {

                    // Valid substring length
                    int length = i - st.top();

                    maxLength = max(maxLength, length);
                }
            }
        }

        return maxLength;
    }
};