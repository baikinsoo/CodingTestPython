from collections import deque

# stack은 LIFO로 마지막에 들어간게 가장 첫번째로 꺼내져야 한다.
class MyStack(object):
    def __init__(self):
        self.q = deque()

    # 넣을 때는 Last In 뽑을 때는 First Out이 되어야 하기 때문에 순서를 바꾼다.
    def push(self, value):
        self.q.append(value)
        # 값을 넣고 해당 값이 Queue 형태로 제일 먼저 뽑힐 때 들어간 반대 방향에서 뽑히기 때문에 순서를 바꾼다.
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    # 큐에서 꺼낼때는 넣은 반대 방향에서 꺼내기 때문에 popleft()를 이용하여 꺼낸다.
    def pop(self):
        return self.q.popleft()

    # stack에서 top은 가장 먼저 꺼내질 Node이기 때문에 큐에서는 0번째 인덱스가 top에 해당한다.
    def top(self):
        if not self.empty():
            return self.q[0]
        else:
            return None

    # 비어있을 때는 deque의 길이가 0인지 확인하면 된다.
    def empty(self):
        return len(self.q) == 0

stack = MyStack()

stack.push(3)
stack.pop()
print(stack.top())



