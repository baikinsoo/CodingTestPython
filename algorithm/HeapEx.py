class BinaryMaxHeap:
    def __init__(self):
        # 계산 편의를 위해 첫번째 인덱스는 0이 아니라 1로 둔다.
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    # _ 하나만 쓰는 이유는 클래스 안에서만 사용하기 위해서 작성한 것이다.
    def _percolate_up(self):
        # 전체 길이를 구하면 마지막 원소를 가르키기 때문이다.
        cur = len(self)
        # 2로 나누고 나머지를 버리면 자신의 부모를 가르키게 된다.
        parent = cur // 2

        # 부모 인덱스와 값을 변경
        while parent > 0:
            if self.items[cur] > self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            # 현재 인덱스를 부모의 위치와 변경
            cur = parent
            # 또 부모의 인덱스를 찾기
            parent = cur // 2

    def _percolate_down(self, cur):

        biggest = cur
        left =  2 * cur
        right = 2 * cur + 1

        if left <= len(self) and self.items[left] > self.items[biggest]:
            biggest = left

        if right <= len(self) and self.items[right] > self.items[biggest]:
            biggest = right

        if biggest != cur:
            self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
            self._percolate_down(biggest)


    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def extract(self):

        if len(self) < 1:
            return None
        # 최대일 경우 가장 큰 수 최소일 경우 가장 작은 수를 꺼낸다.
        root = self.items[1]

        # 맨앞과 맨뒤의 위치를 변경한다.
        self.items[1] = self.items[-1]

        # 맨뒤의 값을 꺼낸다. => 맨 앞에 있던 값
        self.items.pop()

        # 계속 내린다.
        self._percolate_down(1)

        # 꺼낸 값을 반환한다.
        return root




