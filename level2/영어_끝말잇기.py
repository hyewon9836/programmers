def solution(n, words):
    lst = []
    lst.append(words[0])
    for i in range(1,len(words)):
        if lst[-1][-1]!=words[i][0] or words[i] in lst:
            return [i%n+1,i//n+1]
        lst.append(words[i])
    return [0,0]