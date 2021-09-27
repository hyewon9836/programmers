import heapq
def solution(scovile,K):
    answer=0
    heap=[]
    for num in scovile:
        heapq.heappush(heap,num)
    while True:
        check=heapq.heappop(heap)
        if len(heap)==1:
            return -1
        if check>=K:
            break
        heapq.heappush(heap,check)
        min_1=heapq.heappop(heap)
        min_2=heapq.heappop(heap)
        heapq.heappush(heap,min_1+min_2*2)
        answer+=1
    return answer