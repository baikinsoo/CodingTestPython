from collections import deque

deck = deque()          # 신규 데크 생성 ([])
deck.append(1)          # 오른쪽 끝에 1을 삽입 ([1])
deck.appendleft(2)      # 왼쪽 끝에 2를 삽입 ([2, 1])
deck.append(3)          # 오른쪽 끝에 3을 삽입 ([2, 1, 3])
a = deck.pop()          # 오른쪽 끝에서 삭제 후 a에 그 값을 저장 ([2, 1])
print(a)                # 3
b = deck.popleft()      # 왼쪽 끝에서 삭제 후 b에 그 값을 저장 ([1])
print(b)                # 2