def solution(priorities,location):
    answer=0
    num_idx=[i for i in range(len(priorities))]
    while len(priorities)>0:
        max_num=max(priorities)
        num=priorities[0]
        if num==max_num:
            priorities.pop(0)
            check=num_idx.pop(0)
            answer+=1
            if location==check:
                return answer
        else:
            priorities.append(priorities.pop(0))
            num_idx.append(num_idx.pop(0))
    return answer

priorities=[1,1,9,1,1,1]
location=0
print(solution(priorities,location))