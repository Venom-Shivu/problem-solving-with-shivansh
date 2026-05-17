class Solution {
public:

    bool isValidSudoku(vector<vector<char>>& board) {

        // rows[i][num] -> num exists in row i
        bool rows[9][9] = {false};

        // cols[i][num] -> num exists in col i
        bool cols[9][9] = {false};

        // boxes[i][num] -> num exists in box i
        bool boxes[9][9] = {false};

        for (int row = 0; row < 9; row++) {

            for (int col = 0; col < 9; col++) {

                char current = board[row][col];

                // Skip empty cells
                if (current == '.') {
                    continue;
                }

                // Convert char digit to index (0-8)
                int num = current - '1';

                // Calculate box index
                int boxIndex = (row / 3) * 3 + (col / 3);

                // Duplicate found
                if (rows[row][num] ||
                    cols[col][num] ||
                    boxes[boxIndex][num]) {

                    return false;
                }

                // Mark digit as seen
                rows[row][num] = true;
                cols[col][num] = true;
                boxes[boxIndex][num] = true;
            }
        }

        return true;
    }
};