from itertools import combinations


def solution(relation):
    n = len(relation[0])
    combi = []
    for i in range(1, n + 1):
        combi += combinations(range(n), i)
    check = []
    for idx in combi:
        flag = False
        lst = []
        for person in relation:
            a = []
            for i in idx:
                a.append(person[i])
            lst.append(tuple(a))
        if len(set(lst)) == len(relation):
            flag = True

        for c in check:
            if set(c).issubset(idx):
                flag = False
                break

        if flag == True:
            check.append(idx)
    return len(check)