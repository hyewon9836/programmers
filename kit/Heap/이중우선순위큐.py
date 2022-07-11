import heapq
def solution(operations):
    heap=[]
    while(operations):
        oper,num=operations.pop(0).split()
        num=int(num)
        if oper=='I':
            heapq.heappush(heap,num)
        elif heap:
            if num==-1:
                heapq.heappop(heap)
                print(heap)
            else:
                heap.remove(max(heap))
                print(heap)
    if len(heap)==0:
        return [0,0]
    else:
        return [max(heap),heap[0]]
