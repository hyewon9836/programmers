def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)
    lst = {}
    check = {}

    for id in report:
        id_1, id_2 = id.split(' ')

        if id_2 not in check:
            check[id_2] = 1
        else:
            check[id_2] += 1

        if id_1 not in lst:
            lst[id_1] = [id_2]
        else:
            if id_2 not in lst[id_1]:
                lst[id_1] += [id_2]

    for id, cnt in check.items():
        print(id, cnt)
        if cnt >= k:
            for user, user_lst in lst.items():
                if id in user_lst:
                    answer[id_list.index(user)] += 1
    return answer