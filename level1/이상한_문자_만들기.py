def solution(s):
    answer = ''
    i=0;flag=0;
    while 1:
        if s[i]==' ':
            answer+=' '
            flag=0
        elif flag%2==1:
            answer+=s[i].lower()
            flag+=1
        elif flag%2==0:
            answer+=s[i].upper()
            flag+=1
        if len(answer)==len(s):
            break
        i+=1
    return answer