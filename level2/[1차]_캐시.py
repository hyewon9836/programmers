from collections import deque
def solution(cacheSize, cities):
    answer = 0
    que=deque()
    if cacheSize==0:
        return len(cities)*5
    for city in cities:
        city=city.lower()
        if city not in que:
            answer+=5
            if len(que)<cacheSize:
                que.append(city)
            else:
                que.popleft()
                que.append(city)
        else:
            que.remove(city)
            que.append(city)
            answer+=1
    return answer