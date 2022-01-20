import datetime
def solution(lines):
    dateformat="%Y-%m-%d %H:%M:%S.%f"
    answer=0
    end=[];start=[]
    for i,time in enumerate(lines):
        endtime=time[:23]
        end.append(datetime.datetime.strptime(endtime,dateformat))
        gap=(float)(time[23:-1])
        start.append(end[i]-datetime.timedelta(seconds=gap)+datetime.timedelta(seconds=0.001))
    for i in range(len(lines)):
        cnt=0
        for j in range(i,len(lines)):
            if end[i]>start[j]-datetime.timedelta(seconds=1):
                cnt+=1
        answer=max(answer,cnt)
    return answer