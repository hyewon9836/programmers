def solution(m, n, board):
    answer = 0
    for i in range(len(board)):
        board[i] = list(board[i])

    while True:
        array = [[0] * n for i in range(m)]
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != 0 and board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j] and board[i][
                    j] == board[i + 1][j + 1]:
                    array[i][j], array[i + 1][j], array[i][j + 1], array[i + 1][j + 1] = 1, 1, 1, 1
        cnt = 0
        for i in range(m):
            cnt += sum(array[i])
        answer += cnt
        if cnt == 0:
            break
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if array[i][j] == 1:
                    x = i - 1
                    while x >= 0 and array[x][j] == 1:
                        x -= 1
                    if x < 0:
                        board[i][j] = 0
                    else:
                        board[i][j] = board[x][j]
                        array[x][j] = 1
    return answer