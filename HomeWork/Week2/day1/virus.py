'''
같은 네트워크에 있으면 전부 감연된다.
dfs에 컴퓨터를 넣으면 하위 컴퓨터를 확인하고, 감염 시킨다.
for문으로 돌면서 감염되었는지 확인하고 감연안되었다면 감염 시킴과 동시에 count를 올린다.
종료 조건은...
'''
import sys
# 컴 숫자
com = int(input())
# 쌍 숫자
keyValue = int(input())
# 현재 네트워크 구성
network = [[] for i in range(com+1)]
# 방문한 컴퓨터인지 확인
virusCom = [0]*(com+1)
# 각 컴퓨터와 연결된 컴퓨터 list를 각 인덱스에 list로 넣는다.
for _ in range(keyValue):
    n, m = map(int, sys.stdin.readline().split())
    network[n].append(m)
    network[m].append(n)

# 반복해야 할 로직
# 1. 특정 값이 들어오면 해당 값이 어떤 리스트를 가지고 있는 지 보고 해당 리스트를 전부 확인해야 한다.
# 컴퓨터를 넣으면
def dfs(computer):
    # 우선 감염시키고
    virusCom[computer] = 1
    # 해당 컴퓨터와 연결된 컴퓨터 확인
    for linkedComputer in network[computer]:
        # 감염 안된 컴퓨터면 dfs를 통해 감염시키고 계속 돌면서 확인
        if virusCom[linkedComputer] == 0:
            dfs(linkedComputer)

dfs(1)
print(sum(virusCom)-1)

















