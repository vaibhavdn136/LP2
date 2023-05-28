def solve(board, row, cols, ndiag, rdiag, asf):
    global count
    if row == len(board):
        solutions.append(asf)
        count += 1
        return

    for clm in range(len(board[0])):
        if not cols[clm] and not ndiag[row + clm] and not rdiag[row - clm + len(board) - 1]:
            board[row][clm] = True
            cols[clm] = True
            ndiag[row + clm] = True
            rdiag[row - clm + len(board) - 1] = True
            solve(board, row + 1, cols, ndiag, rdiag, asf + str(row) + "-" + str(clm) + " ,")
            cols[clm] = False
            ndiag[row + clm] = False
            rdiag[row - clm + len(board) - 1] = False


print("Please enter the number of queens you want:")
try:
    n = int(input())
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

if n <= 0:
    print("Invalid input. Number of queens should be a positive integer.")
    exit()

board = [[False] * n for _ in range(n)]
cols = [False for _ in range(n)]
ndiag = [False for _ in range(2 * n - 1)]
rdiag = [False for _ in range(2 * n - 1)]
count = 0
solutions = []

solve(board, 0, cols, ndiag, rdiag, "")

print("The total number of possible outcomes is:", count)
print("Solutions:")

# Convert solutions to a matrix form
for solution in solutions:
    matrix = [['-' for _ in range(n)] for _ in range(n)]
    positions = solution.split(',')
    for position in positions:
        if position.strip():
            row, col = map(int, position.split('-'))
            matrix[row][col] = 'Q'
    for row in matrix:
        print(' '.join(row))
    print()
