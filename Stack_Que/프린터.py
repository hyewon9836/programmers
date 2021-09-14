def solution(priorities, location):
    target=priorities.copy()
    answer=1
    target[location]='target'
    while(priorities):
        max_num=max(priorities)
        num=priorities.pop(0)
        if num == max_num:
            if target[0]=='target':
                break
            else:
                target.pop(0)
                answer+=1
        else:
            priorities.append(num)
            target.append(target.pop(0))
    return answer
