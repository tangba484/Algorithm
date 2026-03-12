board = []

for _ in range(9):
    board.append(list(map(int,input().split())))

arr = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            arr.append([i,j])


def check(x,y,num):
    for i in range(9):
        if board[x][i] == num:
            return False
    for i in range(9):
        if board[i][y] == num:
            return False
    bx = x//3 * 3
    by = y//3 * 3
    for nx in range(bx,bx + 3):
        for ny in range(by,by + 3):
            if board[nx][ny] == num:
                return False
    return True

def back(idx):
    if idx == len(arr):
        for i in board:
            print(*i)
        return True
    
    x,y = arr[idx]

    for i in range(1,10):
        if check(x,y,i):
            board[x][y] = i
            if back(idx + 1):
                return True
            board[x][y] = 0

    return False

back(0)