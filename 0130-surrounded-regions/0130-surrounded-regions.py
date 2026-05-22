class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            stack = [(r, c)]

            while stack:
                x, y = stack.pop()

                if (x < 0 or x >= rows or
                    y < 0 or y >= cols or
                    board[x][y] != 'O'):
                    continue

                board[x][y] = '#'

                stack.append((x + 1, y))
                stack.append((x - 1, y))
                stack.append((x, y + 1))
                stack.append((x, y - 1))

        # Left + Right borders
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)

            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)

        # Top + Bottom borders
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)

            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)

        # Final conversion
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'