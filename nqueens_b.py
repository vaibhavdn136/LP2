def isSafe(chess, row, col):
    r = row
    c = col

    # Upper column check
    while row >= 0:
        if chess[row][col] == 1:
            return False
        row -= 1
    
    row = r
    col = c

    # Upper left diagonal check
    while row >= 0 and col >= 0:
        if chess[row][col] == 1:
            return False
        row -= 1
        col -= 1
    
    row = r
    col = c

    # Upper right diagonal check
    while row >= 0 and col < len(chess):
        if chess[row][col] == 1:
            return False
        row -= 1
        col += 1
    
    return True


def solveNQueens(n):
    def printSolution(chess):
        matrix = [['.' for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if chess[i][j] == 1:
                    matrix[i][j] = 'Q'
        return matrix

    def solveNQueensUtil(chess, row, result):
        if row == n:
            result.append(printSolution(chess))
            return

        for col in range(n):
            if isSafe(chess, row, col):
                chess[row][col] = 1
                solveNQueensUtil(chess, row + 1, result)
                chess[row][col] = 0

    chess = [[0] * n for _ in range(n)]
    result = []
    solveNQueensUtil(chess, 0, result)
    return result


n = int(input("Enter the value of N: "))
solutions = solveNQueens(n)

print("Total solutions:", len(solutions))
for solution in solutions:
    for row in solution:
        print(" ".join(row))
    print()
