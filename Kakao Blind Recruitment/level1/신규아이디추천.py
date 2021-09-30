import re
def solution(new_id):
    answer=new_id.lower()
    answer=re.sub(r"[^a-zA-Z0-9_.-]","",answer)
    while('..' in answer):
        answer=answer.replace('..','.')
    while len(answer)>0:
        if answer[0]!='.' and answer[-1]!='.':
            break
        if answer[0]=='.':
            answer=answer[1:]
        if len(answer)>0 and answer[-1]=='.':
            answer=answer[:-1]
    if len(answer)==0:
        answer='a'
    elif len(answer)>=16:
        answer=answer[:15]
        if answer[-1]=='.':
            answer=answer[:14]
    while(len(answer)<3):
        answer=answer+answer[-1]
    return answer