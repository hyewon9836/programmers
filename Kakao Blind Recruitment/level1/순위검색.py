from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []
    info_dict = {}

    for i in range(len(info)):
        info_lst = info[i].split()
        key = info_lst[:-1]
        val = info_lst[-1]

        for j in range(5):
            for c in combinations(key, j):
                tmp = "".join(c)
                if tmp in info_dict:
                    info_dict[tmp].append(int(val))
                else:
                    info_dict[tmp] = [int(val)]
    for k in info_dict:
        info_dict[k].sort()

    for qu in query:
        qu_lst = qu.split(' ')
        qu_key = qu_lst[:-1]
        qu_val = qu_lst[-1]

        while 'and' in qu_key:
            qu_key.remove('and')
        while '-' in qu_key:
            qu_key.remove('-')
        qu_key = ''.join(qu_key)

        if qu_key in info_dict:
            scores = info_dict[qu_key]
            if scores:
                enter = bisect_left(scores, int(qu_val))
                answer.append(len(scores) - enter)
        else:
            answer.append(0)
    return answer