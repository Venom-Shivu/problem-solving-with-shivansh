from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        # Pruning: frequency check
        board_count = Counter(c for row in board for c in row)

        for ch, freq in Counter(word).items():
            if board_count[ch] < freq:
                return False

        # Start from rarer character side
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        def dfs(r, c, idx):
            if idx == len(word):
                return True

            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[idx]):
                return False

            temp = board[r][c]
            board[r][c] = "#"   # mark visited

            found = (
                dfs(r+1, c, idx+1) or
                dfs(r-1, c, idx+1) or
                dfs(r, c+1, idx+1) or
                dfs(r, c-1, idx+1)
            )

            board[r][c] = temp   # backtrack
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False