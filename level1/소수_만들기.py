from itertools import combinations
def solution(nums):
    answer = 0
    comb=list(combinations(nums, 3))
    for i in comb:
        num=sum(i)
        for j in range(2,num):
            if num%j==0:
                break
        else:
            answer+=1
    return answer