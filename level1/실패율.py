def solution(N,stages):
    answer={}
    player=len(stages)
    for stage in range(1,N+1):
        if player!=0:
            cnt=stages.count(stage)
            answer[stage]=cnt/player
            player-=cnt
        else:
            answer[stage]=0
    return sorted(answer,key=lambda x: answer[x],reverse=True)