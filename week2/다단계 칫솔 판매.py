"""
유형 : 트리 탐색

주어진 변수로 트리를 생성한 후 dfs를 활용해 트리 탐색
주어진 조건이 맞을 때만 부모 노드 방문
"""

def solution(enroll, referral, seller, amount):
    answer = {name:0 for name in enroll}
    parents = {child:parent for parent, child in zip(referral, enroll)}

    def dfs(cur, earn):
        nonlocal answer
        if earn < 1:
            return
        else:
            ten = int(earn * 0.1)
            earn -= ten
            answer[cur] += earn

            if parents[cur] != '-':
                dfs(parents[cur], ten)

    for s, a in zip(seller, amount):
        dfs(s, a*100)

    return list(answer.values())
