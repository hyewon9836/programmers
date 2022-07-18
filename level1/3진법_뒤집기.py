def solution(n):
    answer = 0
    lst=[]
    while n>=1:
        lst.append(n%3)
        n=n//3
    for i in range(len(lst)):
        answer+=lst[len(lst)-1-i]*(3**i)
    return answer