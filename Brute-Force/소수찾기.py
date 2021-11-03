from itertools import permutations

def solution(numbers):
    answer=0
    number_lst=[]
    for i in range(len(numbers)):
        num=list(permutations(numbers,i+1))
        number_lst+=[int(''.join(i)) for i in num]
    for num in set(number_lst):
        tmp=0
        for i in range(1,num+1):
            if num%i==0 and num!=0:
                tmp+=1
            if tmp>=3:
                break
        if tmp==2:
            answer+=1
    return answer
