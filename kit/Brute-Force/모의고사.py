def solution(answers):
    answer=[]
    lst1=[1,2,3,4,5]
    lst2=[2,1,2,3,2,4,2,5]
    lst3=[3,3,1,1,2,2,4,4,5,5]
    cnt1=0;cnt2=0;cnt3=0
    for i in range(len(answers)):
        if answers[i]==lst1[i%len(lst1)]:
            cnt1+=1
        if answers[i]==lst2[i%len(lst2)]:
            cnt2+=1
        if answers[i]==lst3[i%len(lst3)]:
            cnt3+=1
    cnt_lst=[cnt1,cnt2,cnt3]
    for idx, cnt in enumerate(cnt_lst):
        if cnt==max(cnt_lst):
            answer.append(idx+1)
    return answer
