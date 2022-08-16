def solution(grid):
    answer = []
    dy = [1, 0, -1, 0]
    dx = [0, -1, 0, 1]
    len_y, len_x = len(grid), len(grid[0])
    visited = [[[0] * 4 for i in range(len_x)] for j in range(len_y)]
    for y in range(len_y):
        for x in range(len_x):
            for d in range(4):
                if visited[y][x][d]:
                    continue
                count = 0
                ny, nx = y, x
                while not visited[ny][nx][d]:
                    visited[ny][nx][d] = 1
                    count += 1
                    if grid[ny][nx] == "S":
                        pass
                    elif grid[ny][nx] == "L":
                        d = (d - 1) % 4
                    elif grid[ny][nx] == "R":
                        d = (d + 1) % 4
                    ny = (ny + dy[d]) % len_y
                    nx = (nx + dx[d]) % len_x
                answer.append(count)
    return sorted(answer)
