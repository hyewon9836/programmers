from collections import deque
def solution(queue1, queue2):
    answer = 0
    que1=deque(queue1)
    que2=deque(queue2)
    sum1=sum(que1)
    sum2=sum(que2)
    if (sum1+sum2)%2==1:
        return -1
    for i in range(len(que1)*3):
        if sum1>sum2:
            num=que1.popleft()
            sum1-=num
            que2.append(num)
            sum2+=num
        elif sum1<sum2:
            num=que2.popleft()
            sum2-=num
            que1.append(num)
            sum1+=num
        elif sum1==sum2:
            return answer
        answer+=1
    return -1