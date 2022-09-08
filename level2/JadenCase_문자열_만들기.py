def solution(s):
    answer = ''
    for word in s.lower().split(' '):
        if word=='':
            answer+=' '
        else:
            answer+=word[0].upper()+word[1:].lower()
            answer+=' '
    return answer[:-1]