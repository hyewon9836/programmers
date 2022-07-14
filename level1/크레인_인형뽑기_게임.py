def solution(board, moves):
    bucket = []
    answer = 0
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] > 0:
                bucket.append(board[i][move-1])
                board[i][move-1] = 0
                if len(bucket)>1:
                    if bucket[-1] == bucket[-2]:
                        answer += 2
                        bucket = bucket[:-2]
                break
    return answer