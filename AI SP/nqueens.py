def isSafe(row, col):
    global board
    for i in range(col, -1, -1):
        if(board[row][i]):
            return False
        
    for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
        if(board[i][j]):
            return False
        
    for i,j in zip(range(row, n, 1), range(col, -1, -1)):
        if(board[i][j]):
            return False
        
    return True

def printBoard():
    global board
    for i in range(n):
        for j in range(n):
            if(board[i][j]):
                print("Q", end="")
            else:
                print(". ", end="")
        print()
    
def solve(board, col):
    global n
    if(col==n):
        printBoard()
        # print(board)
        return True
    for row in range(n):
        if(isSafe(row,col)):
            board[row][col] = 1
            if(solve(board, col+1)):
                return True
            board[row][col] = 0

def main():
    global n, board
    n = int(input("Enter number of queens : "))
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve(board, 0)

main()
