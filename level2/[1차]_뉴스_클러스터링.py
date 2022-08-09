def solution(str1, str2):
    str1=str1.lower(); str2=str2.lower()
    lst1=[]; lst2=[]
    for i in range(0,len(str1)-1):
        if str1[i:i+2].isalpha():
            lst1.append(str1[i:i+2])
    for i in range(0,len(str2)-1):
        if str2[i:i+2].isalpha():
            lst2.append(str2[i:i+2])
    gyo=set(lst1)&set(lst2); hap=set(lst1)|set(lst2)
    gyo_cnt=sum([min(lst1.count(i),lst2.count(i))for i in gyo])
    hap_cnt=sum([max(lst1.count(i),lst2.count(i))for i in hap])
    if gyo_cnt ==0 and hap_cnt ==0:
        return 65536
    elif gyo_cnt==0:
        return 0
    else:
        return int((gyo_cnt/hap_cnt)*65536)