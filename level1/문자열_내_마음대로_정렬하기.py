def solution(strings, n):
    dic = {}
    answer=[]
    strings.sort()
    for i,string in enumerate(strings):
        dic[i]=string[n]
    dic=sorted(dic.items(),key=lambda x :x[1])
    for idx,value in dic:
        answer.append(strings[idx])
    return answer