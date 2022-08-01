import collections
def solution(numbers,target):
    answer=0
    stack=collections.deque([(0,0)])
    while stack:
        sum,idx=stack.popleft()
        if idx==len(numbers):
            if sum==target:
                answer+=1
        else:
            number=numbers[idx]
            stack.append((sum+number,idx+1))
            stack.append((sum-number,idx+1))
    return answer
