import re
def solution(dartResult):
    idx=0
    num=re.findall('\d+',dartResult)
    num=list(map(int,num))
    for i in dartResult:
        if i.isdigit()==False:
            if i=="S":
                idx+=1
            elif i=="D":
                num[idx]=num[idx]**2
                idx+=1
            elif i=="T":
                num[idx]=num[idx]**3
                idx+=1
            elif i=="*":
                num[idx-1]=num[idx-1]*2
                if idx>1:
                    num[idx-2]=num[idx-2]*2
            elif i=='#':
                num[idx-1]=num[idx-1]*(-1)
    return sum(num)