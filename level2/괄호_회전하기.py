def solution(s):
    answer=0
    lst=list(s)
    for _ in range(len(s)):
        que=[]
        for i in range(len(lst)):
            if len(que)>0:
                if que[-1]=='[' and lst[i]==']':
                    que.pop()
                elif que[-1]=='(' and lst[i]==')':
                    que.pop()
                elif que[-1]=='{' and lst[i]=='}':
                    que.pop()
                else:
                    que.append(lst[i])
            else:
                que.append(lst[i])
        if len(que)==0:
            answer+=1
        lst.append(lst.pop(0))
    return answer