def solution(n,lost,reserve):
    reserve_lst=set(reserve)-set(lost)
    lost_lst=set(lost)-set(reserve)
    for i in reserve_lst:
        if i-1 in lost_lst:
            lost_lst.remove(i-1)
        elif i+1 in lost_lst:
            lost_lst.remove(i+1)
    return n-len(lost_lst)
