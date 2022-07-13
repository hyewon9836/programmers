def solution(numbers, hand):
    answer = ''
    number={1:[0,0],2:[0,1],3:[0,2],
            4:[1,0],5:[1,1],6:[1,2],
            7:[2,0],8:[2,1],9:[2,2],
            '*':[3,0],0:[3,1],'#':[3,2]}
    left=number['*']; right=number['#']
    for num in numbers:
        now=number[num]
        if num in [1,4,7]:
            answer+='L'
            left=now
        elif num in [3,6,9]:
            answer+='R'
            right=now
        else:
            left_dis=abs(left[0]-now[0])+abs(left[1]-now[1])
            right_dis=abs(right[0]-now[0])+abs(right[1]-now[1])
            if left_dis<right_dis:
                answer+='L'
                left=now
            elif left_dis>right_dis:
                answer+='R'
                right=now
            else:
                if hand=='left':
                    answer+='L'
                    left=now
                else:
                    answer+='R'
                    right=now
    return answer

numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand='right'
print(solution(numbers,hand))