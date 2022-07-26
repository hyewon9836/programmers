def solution(n, m):
    a,b=max(n,m),min(n,m)
    rest=1
    while rest>0:
        rest=a%b
        a,b=b,rest
    return [a,int(n*m/a)]