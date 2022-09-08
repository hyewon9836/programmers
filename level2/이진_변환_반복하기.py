def solution(s):
    cnt_2=0; cnt_0=0
    while s!='1':
        cnt_0+=s.count('0')
        s=bin(len(s)-s.count('0'))[2:]
        cnt_2+=1
    return [cnt_2, cnt_0]