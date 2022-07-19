from itertools import combinations
def solution(numbers):
    answer = []
    lst=list(combinations(numbers,2))
    for (a,b) in lst:
        answer.append(a+b)
    return sorted(list(set(answer)))