from collections import deque
def solution(maps):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    row=len(maps)
    col=len(maps[0])
    flag=[[-1 for _ in range(col)] for _ in range(row)]
    que=deque()
    que.append([0,0])
    flag[0][0]=1
    while que:
        y,x=que.popleft()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=ny<row and 0<=nx<col and maps[ny][nx]==1:
                if flag[ny][nx]==-1:
                    flag[ny][nx]=flag[y][x]+1
                    que.append([ny,nx])
    return flag[-1][-1]