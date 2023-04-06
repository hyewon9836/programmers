def solution(progresses,speeds):
    answer=[]
    while len(progresses)>0:
        cnt=0
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
        for i in range(len(progresses)):
            if progresses[0]>=100:
                progresses.pop(0)
                speeds.pop(0)
                cnt+=1
        if cnt>0:
            answer.append(cnt)
    return answer

progresses=[95, 90, 99, 99, 80, 99]	
speeds=[1, 1, 1, 1, 1, 1]	
print(solution(progresses,speeds))