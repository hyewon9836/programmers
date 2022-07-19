def solution(sizes):
    max_s=[];min_s=[]
    for size in sizes:
        max_s.append(max(size))
        min_s.append(min(size))
    return max(max_s)*max(min_s)