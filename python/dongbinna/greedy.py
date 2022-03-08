# 단순히 매 순간마다 큰 값을 고르는 것!

# 그리디 알고리즘 --> 문제 풀이를 위한 최소한의 아이디어를 떠올리는것이 중요

# 모험가 길드

# 공포도가 작은사람이 많으면 팀 수 증가 굿 == 오름차순
# ==> N 이하

# 내 풀이


N = int(input())
scary = list(map(int, input().split()))

# sorted(scary)
scary.sort()

# fix_idx = 0
# mv_idx = 0
# team = 0

# while mv_idx != N:
#     elem = scary(fix_idx)

# 동빈나 풀이

result = 0
count = 0

for i in scary:  # 낮은 공포도부터 확인
    count += 1  # 모험가 증가
    if count >= i:  # 모험가 수 가 현재 공포도 이상이라면 팀 결성
        result += 1  # 팀 수 증가
        count = 0  # 모험가 초기화
print(result)
