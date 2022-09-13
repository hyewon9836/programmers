def solution(n):
    answer=1
    for i in range(1,n//2+1):
        cnt=0
        for j in range(i,n):
            cnt+=j
            if cnt==n:
                answer+=1
                break
            elif cnt>n:
                break
    return answer