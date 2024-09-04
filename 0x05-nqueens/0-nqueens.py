[200~  # !/usr/bin/python3
        import sys

        def is_safe(board, row, col):
            """
                Check if it's safe to place a queen at board[row][col]
                    This means checking the row, column, and diagonals.
                        """
                            for i in range(col):
                                    if board[row][i] == 1:
                                                return False

                                                    for i, j in zip(
                                                        range(row, -1, -1), range(col, -1, -1)):
                                                            if board[i][j] == 1:
                                                                        return False

                                                                            for i, j in zip(
                                                                                range(row, len(board), 1), range(col, -1, -1)):
                                                                                    if board[i][j] == 1:
                                                                                                return False

                                                                                                    return True

                                                                                                    def solve_nqueens(
                                                                                                        board, col, results):
                                                                                                        """
                                                                                                            Solves the N Queens problem using backtracking.
                                                                                                                """
                                                                                                                    if col >= len(
                                                                                                                        board):
                                                                                                                            results.append(
                                                                                                                                [[i, row.index(1)] for i, row in enumerate(board)])
                                                                                                                                    return True

                                                                                                                                        for i in range(
                                                                                                                                            len(board)):
                                                                                                                                            if is_safe(
                                                                                                                                                board, i, col):
                                                                                                                                                            board[i][col]= 1
                                                                                                                                                                        solve_nqueens(
                                                                                                                                                                            board, col + 1, results)
                                                                                                                                                                                    board[i][col]= 0

                                                                                                                                                                                        return False

                                                                                                                                                                                        def print_solutions(
                                                                                                                                                                                            n):
                                                                                                                                                                                            """
                                                                                                                                                                                                Initializes the board and starts the backtracking process.
                                                                                                                                                                                                    """
                                                                                                                                                                                                        board= [[0 for _ in range(n)] for _ in range(n)]
                                                                                                                                                                                                            results= []
                                                                                                                                                                                                                solve_nqueens(
                                                                                                                                                                                                                    board, 0, results)
                                                                                                                                                                                                                    for solution in results:
                                                                                                                                                                                                                            print(
                                                                                                                                                                                                                                solution)

                                                                                                                                                                                                                            if __name__ == "__main__":
                                                                                                                                                                                                                                if len(
                                                                                                                                                                                                                                    sys.argv) != 2:
                                                                                                                                                                                                                                        print(
                                                                                                                                                                                                                                            "Usage: nqueens N")
        sys.exit(1)

                try:
                            n= int(sys.argv[1])
                                except ValueError:
                                            print("N must be a number")
                                                    sys.exit(1)

                                                        if n < 4:
                                                                    print(
                                                                        "N must be at least 4")
                                                                            sys.exit(
                                                                                1)

                                                                                print_solutions(
                                                                                    n)
