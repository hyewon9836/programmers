def solution(record):
    answer=[]
    dic={}
    for rec in record:
        rec_lst=rec.split()
        if len(rec_lst)==3:
            dic[rec_lst[1]]=rec_lst[2]
    for rec in record:
        rec_lst=rec.split()
        if rec_lst[0]=="Enter":
            answer.append("%s님이 들어왔습니다."%dic[rec_lst[1]])
        elif rec_lst[0]=="Leave":
            answer.append("%s님이 나갔습니다."%dic[rec_lst[1]])
    return answer