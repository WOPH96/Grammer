# 구현 => 풀이를 떠올리는 것은 쉽지만 소스코르도 옮기기 어려운 문제

# 알고리즘은 간단한데 코드가 지나칠만큼 길어지는 문제
# 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
# 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
# 적절한 라이브러리를 찾아서 사용해야 하는 문제 eg) 순열, 조합

# 많은 코드를 작성하고 많은 라이브러리를 사용해본다면 쉽게 풀 수 있음.

# 상하좌우

# Simulation 유형 / 완전 탐색 / 구현 유형

# (1,1) 시작하여 (100,100)
# R ==> (1,2) dy = 1 , L==> (1,0) dy = -1
# U ==> (2,1)

n = int(input())

x, y = 1, 1  # (1,1) 에서 시작

# plans = str(input()) #문자열로 받을때 eg) RUDRLLRUD
plans = input().split()  # 띄어쓰기로 받을 때(리스트) eg) R U D D L U

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    i = move_types.index(plan)
    x += dx[i]
    y += dy[i]

    if(x < 1 or y < 1 or x > n or y > n):
        x -= dx[i]
        y -= dy[i]


print(f"({x},{y})")

# 동빈나

for plan in plans:
    i = move_types.index(plan)

    tx = x + dx[i]
    ty = y + dy[i]
    if(tx < 1 or ty < 1 or tx > n or ty > n):
        continue

    x += dx[i]
    y += dy[i]

print(f"({x},{y})")
