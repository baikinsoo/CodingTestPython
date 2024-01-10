import sys

def top():
    # 타워 수
    n = int(sys.stdin.readline().rstrip())
    # 타워 높이 리스트로 출력
    topList = list(map(int, sys.stdin.readline().rstrip().split()))

    #
    topStack = []
    answer = []

    for i in range(n):
        # 보이는 타워가 있으면
        while topStack:
            # 보이는 타워 중 가장 가까운 타워와 현재 타워 비교

            # 앞에 타워가 크면 해당 타워 인덱스 정답에 넣기
            if topStack[-1][1] > topList[i]:
                answer.append(topStack[-1][0] + 1)
                # 최초 보이는 타워만 넣을 거임
                break
            # 앞에 타워가 작으면 뒤에 타워도 볼 일 없음
            else:
                # 업애버리면 된다.
                topStack.pop()
        # 첫번째 타워 and 보이는 타워가 없는 경우 answer 0 넣음
        if i == 0 or not topStack :
            answer.append(0)
        # 비교 후 현재 타워 인덱스와 함께 넣기
        topStack.append([i, topList[i]])

    return answer

if __name__ == "__main__":
    result = top()
    print(" ".join(map(str, result)))
