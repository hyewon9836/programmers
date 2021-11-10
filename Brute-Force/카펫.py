def solution(brown,yellow):
    total = brown+yellow
    for i in range(total,2,-1):
        if total%i==0:
            j=total//i
            if yellow==(i-2)*(j-2):
                return [i,j]