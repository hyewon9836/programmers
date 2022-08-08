from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for c in course:
        lst = []
        for order in orders:
            for combi in combinations(order, c):
                menu = ''.join(sorted(combi))
                lst.append(menu)
        sorted_lst = Counter(lst).most_common()
        answer += [menu for menu, cnt in sorted_lst if cnt > 1 and cnt == sorted_lst[0][1]]
    return sorted(answer)
