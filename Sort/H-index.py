def solution(citations):
    n=len(citations)
    while (n>0):
        cnt=0
        for num in citations:
            if num>=n:
                cnt+=1
        if cnt>=n:
            break
        n-=1
    return n