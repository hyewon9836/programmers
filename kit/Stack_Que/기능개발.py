import math
def solution(progresses, speeds):
    day=[]
    for progress,speed in zip(progresses,speeds):
        day.append(math.ceil((100-progress)/speed))
    answer = []
    a=day.pop(0)
    x=1
    while(day):
        b=day.pop(0)
        if a>=b:
            x+=1
        else:
            answer.append(x)
            x=1; a=b
    answer.append(x)
    return answer
