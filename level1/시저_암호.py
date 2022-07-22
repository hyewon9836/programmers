def solution(s, n):
    answer = ''
    for i in s:
        result=ord(i)
        if result>=65 and result<=90:
            result+=n
            if result>90:
                result-=26
        elif result>=97 and result<=122:
            result+=n
            if result>122:
                result-=26
        answer+=chr(result)
    return answer