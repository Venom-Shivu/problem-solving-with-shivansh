class Solution {
public:

    bool rows[9][9] = {false};
    bool cols[9][9] = {false};
    bool boxes[9][9] = {false};

    void solveSudoku(vector<vector<char>>& board) {

        // Initialize tracking arrays
        for (int row = 0; row < 9; row++) {

            for (int col = 0; col < 9; col++) {

                if (board[row][col] != '.') {

                    int num = board[row][col] - '1';

                    rows[row][num] = true;
                    cols[col][num] = true;

                    int boxIndex =
                        (row / 3) * 3 + (col / 3);

                    boxes[boxIndex][num] = true;
                }
            }
        }

        solve(board);
    }

    bool solve(vector<vector<char>>& board) {

        for (int row = 0; row < 9; row++) {

            for (int col = 0; col < 9; col++) {

                // Empty cell found
                if (board[row][col] == '.') {

                    for (char ch = '1'; ch <= '9'; ch++) {

                        int num = ch - '1';

                        int boxIndex =
                            (row / 3) * 3 + (col / 3);

                        // Check validity
                        if (!rows[row][num] &&
                            !cols[col][num] &&
                            !boxes[boxIndex][num]) {

                            // Place digit
                            board[row][col] = ch;

                            rows[row][num] = true;
                            cols[col][num] = true;
                            boxes[boxIndex][num] = true;

                            // Continue solving
                            if (solve(board)) {
                                return true;
                            }

                            // BACKTRACK
                            board[row][col] = '.';

                            rows[row][num] = false;
                            cols[col][num] = false;
                            boxes[boxIndex][num] = false;
                        }
                    }

                    // No valid number possible
                    return false;
                }
            }
        }

        // Entire board solved
        return true;
    }
};