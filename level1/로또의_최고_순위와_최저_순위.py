def solution(lottos, win_nums):
    idx = 0
    rank = [6, 6, 5, 4, 3, 2, 1]
    zero_cnt = lottos.count(0)
    for num in lottos:
        if num in win_nums:
            idx += 1
    return rank[zero_cnt + idx], rank[idx]