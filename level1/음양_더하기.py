def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i]==False:
            absolutes[i]*=-1
    return sum(absolutes)

'''
def solution(absolutes, signs):
    answer=0
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer
'''



