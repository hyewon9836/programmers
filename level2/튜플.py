def solution(s):
    answer=[]
    s=s[2:-2].split('},{')
    s.sort(key=len)
    for i in s:
        num=i.split(',')
        for j in num:
            if int(j) not in answer:
                answer.append(int(j))
    return answer