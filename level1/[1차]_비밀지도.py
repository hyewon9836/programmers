def solution(n, arr1, arr2):
    answer=[]
    for a,b in zip(arr1,arr2):
        map1=bin(a)[2:].zfill(n)
        map2=bin(b)[2:].zfill(n)
        result=''
        for i in range(n):
            if map1[i]=='1'or map2[i]=='1':
                result+='#'
            else:
                result+=' '
        answer.append(result)
    return answer