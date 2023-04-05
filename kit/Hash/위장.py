def solution(clothes):
    answer=1
    cate_cnt=Counter([cate for name, cate in clothes])
    for cnt in cate_cnt.values():
        answer*=(cnt+1)
    return answer-1

from collections import Counter

clothes=[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))
