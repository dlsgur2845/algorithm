"""
유형 : 해시

1. 장르별 모든 음악과 재생 횟수를 해시에 저장. 장르별 재생 횟수 또한 다른 해시에 저장.
2. 두 해시 모두 정렬
3. 총 재생횟수가 높은 순으로 장르를 pop 해주고 해당 장르에서 높은 순으로 최대 2개까지만 pop해준 결과 값을 answer에 추가
"""

from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_dict = defaultdict(list)
    genre_cnt = defaultdict(int)
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_dict[genre].append((i, play))
        genre_dict[genre] = sorted(genre_dict[genre], key=lambda x:(x[1], -x[0]))
        genre_cnt[genre] += play
    genre_cnt = sorted(genre_cnt.items(), key=lambda x:x[1])
    
    while genre_cnt:
        genre, _ = genre_cnt.pop()
        genre_dict[genre] = genre_dict[genre][-2:]
        
        while genre_dict[genre]:
            answer.append(genre_dict[genre].pop()[0])
            
    return answer
