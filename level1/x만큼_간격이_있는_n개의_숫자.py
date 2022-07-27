def solution(x, n):
    answer = []
    for i in range(x,x*(n+1),x):
        answer.append(i)
    return answer