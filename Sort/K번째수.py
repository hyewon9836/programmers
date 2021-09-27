def solution(array,commands):
    answer=[]
    for lst in commands:
        arr=array[lst[0]-1:lst[1]]
        arr.sort()
        answer.append(arr[lst[2]-1])
    return answer