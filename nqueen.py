class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.solution_count = 0

    def is_safe(self, row, col):
        for prev_row in range(row):
            if (
                self.board[prev_row] == col
                or abs(self.board[prev_row] - col) == abs(prev_row - row)
            ):
                return False
        
    def solve(self, row):
        if row == self.n:
            self.solution_count += 1
            print(f"Solution {self.solution_count}:")
            for r in range(self.n):
                line = ["Q" if self.board[r] == c else "." for c in range(self.n)]
                print(" ".join(line))
            print()
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                self.solve(row + 1)

n_queens_solver = NQueens(8)
n_queens_solver.solve(0)

