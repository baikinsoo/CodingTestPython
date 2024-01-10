'''
1 = 집이 있다
0 = 집이 없다.
단지 = danji
result = [][]
이동을 위한 dx, dy 생성
x축 y축 비교
4군데를 비교했을 때 1이면 0으로 바꾸고, 해당 인덱스는 같은 단지로 인덱스 넣기
하나의 단지가 끝나면 또 돌면서 다음 1을 찾으면 이번에는 2단지르 만들고 똑같이 0으로 만들고 해당 인덱스 2로 저장
'''
import sys

input = sys.stdin.readline

N = int(input())

graph = []  # 입력받을 그래프를 담을 리스트 선언
result = []  # 결과를 담을 리스트 선언
count = 0

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

# 한 점을 기준으로 (위 아래 왼쪽 오른쪽) 으로 한칸 씩 이동할 좌표 설정
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 종료 시점, 반복할 문제
def dfs(x, y):
    global count

    if x < 0 or x >= N or y < 0 or y >= N:
        return

    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

# 그래프의 원소가 1일때만 dfs로 집을 방문한다.
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            dfs(i, j)
            result.append(count)
            count = 0

result.sort()  # 오름차순으로 정렬

print(len(result))  # 총 단지수 출력
for k in result:  # 각 단지마다 집의 수 출력
    print(k)