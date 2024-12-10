def solution(genres, plays):
    answer = []
    total_play = {}
    genre_songs = {}

    for idx, genre in enumerate(genres):
        if genre not in total_play:
            total_play[genre] = 0
            genre_songs[genre] = []
        total_play[genre] += plays[idx]
        genre_songs[genre].append((plays[idx], idx))
    
    sorted_genres = sorted(total_play.items(), key=lambda item: item[1], reverse=True)

    min_length = 999999
    for genre, _ in sorted_genres:
        if min_length > len(genre_songs):
            min_length = len(genre_songs)
    
    for genre, _ in sorted_genres:
    
        sorted_songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
    
        answer.extend([idx for _, idx in sorted_songs[:2]])
    
    return answer
