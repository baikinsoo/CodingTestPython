'''
1. stack으로 queue를 구현하기 위해서는 2개의 스택이 필요하다.
2. peek()이라는 것을 사용하는데 peek()은 queue의 제일 앞 부분을 조회한다.
'''

class MyQueue(object):
    # 두개의 스택을 생성한다.
    def __init__(self):
        self.input = []
        self.output = []

    # 값이 입력되면 input 배열에 값을 넣는다.
    def push(self, value):
        self.input.append(value)

    # 값을 꺼낼 때 peek() 함수를 실행시키고, pop을 통해 값을 꺼낸다.
    def pop(self):
        self.peek()
        self.output.pop()

    # peek() 함수의 경우 input의 값을 꺼내서 output에 넣음으로서 사용자는 큐와 같이 확인 가능하다.
    def peek(self):
        # output이 비어있는지 확인한 뒤
        if not self.output:
            # input에 있는 모든 값을
            while self.input:
                # output에 집어 넣는다 -> 첫번째 스택에 쌓인 값이 또 다른 스택에 들어가면서 순서가 바뀐다. -> LIFO 형태 구현
                self.output.append(self.input.pop())
        # 큐형태가 아닌 list 형태이기 때문에 -1을 통해 끝에 있는 값을 반환한다.
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []

q = MyQueue()

q.push(1)
q.push(2)
q.push(3)

print(q.peek())