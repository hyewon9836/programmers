def solution(n):
    cnt1=bin(n).count('1')
    while 1:
        n+=1
        cnt2=bin(n).count('1')
        if cnt1==cnt2:
            return n