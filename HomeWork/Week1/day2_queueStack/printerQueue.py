from collections import deque

# 테스트 횟수 입력
T = int(input())

# 그냥 반복 실행
for _ in range(T):
    # 문서 갯수와 확인하고 싶은 순서 입력
    N, M = map(int, input().split())

    # 우선순위 입력
    queue = deque(map(int, input().split()))
    # 입력한 우선순위를 기반으로 이중 리스트로 각 문서에 대한 우선 순위 부여
    queue = deque([(value, idx) for idx, value in enumerate(queue)])

    # 순서를 확인 할 count 변수 초기화
    count = 0

    while True:
        # 리스트의 각 첫번째(우선수위) 중 가장 큰 값인지 아닌지 판단
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            # 맞다면 count + 1 즉 순서를 뜻하는 것이다.
            count += 1
            # 만약 해당 우선순위의 문서의 인덱스가 주어진 번호와 같다면 count(순서)를 반환
            if queue[0][1] == M:
                print(count)
                break
            # 만약 주어진 순서와 다른 값이라면 날려 없애버린다.
            else:
                queue.popleft()
        # 만약 제일 큰 값이 아니라면 꺼내서 제일 뒤에 넣는다.
        else:
            queue.append(queue.popleft())