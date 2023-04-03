def solution(plans):
    answer=[]
    stack=[]
    plan=[]
    info=dict()
    for name,start,playtime in plans:
        hour,minute=map(int,start.split(':'))
        playtime=int(playtime)
        start=hour*60+minute
        info[start]=[name,playtime]
        plan.append([name,start,playtime])
    plan.sort(key=lambda x:x[1])
    
    time,cnt=plan[0][1],0

    while cnt<len(plans):
        if stack:
            stack[-1][1]-=1
            if stack[-1][1]==0:
                answer.append(stack[-1][0])
                stack.pop()
                cnt+=1
        if time in info:
            stack.append(info[time])
        time+=1

    return answer


#plans=[["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
#solution(plans)