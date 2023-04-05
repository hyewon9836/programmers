def solution(genres,plays):
    answer=[]
    cnt={}
    for i in range(len(genres)):
        if genres[i] in cnt:
            cnt[genres[i]].append([plays[i],i])
        else:
            cnt[genres[i]]=[[plays[i],i]]    
    
    genre_rank={}
    for genre in cnt.keys():
        play_sum=0
        for song in cnt[genre]:
            play_sum+=song[0]
        genre_rank[genre]=play_sum
    genre_rank=sorted(genre_rank.items(),key=lambda x:-x[1])
    
    for genre in genre_rank:
        song_rank=sorted(cnt[genre[0]],key=lambda x:(-x[0],x[1]))
        genre_max=0
        for song in song_rank:
            answer.append(song[1])
            genre_max+=1
            if genre_max==2:
                break
    return answer

genres=["classic", "pop", "classic", "classic", "pop"]
plays=[500,600,150,800,2500]
print(solution(genres,plays))