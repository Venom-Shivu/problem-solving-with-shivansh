class Solution {
public:

    bool isValidSudoku(vector<vector<char>>& board) {

        // Sets for rows, columns, and boxes
        unordered_set<string> seen;

        for (int row = 0; row < 9; row++) {

            for (int col = 0; col < 9; col++) {

                char current = board[row][col];

                // Ignore empty cells
                if (current == '.') {
                    continue;
                }

                // Create unique identifiers
                string rowKey =
                    "row" + to_string(row) + current;

                string colKey =
                    "col" + to_string(col) + current;

                string boxKey =
                    "box" +
                    to_string((row / 3) * 3 + (col / 3)) +
                    current;

                // Duplicate found
                if (seen.count(rowKey) ||
                    seen.count(colKey) ||
                    seen.count(boxKey)) {

                    return false;
                }

                // Mark as seen
                seen.insert(rowKey);
                seen.insert(colKey);
                seen.insert(boxKey);
            }
        }

        return true;
    }
};