from typing import List

def permute(nums:List[int])->List[int]:
    results = []
    prev_elements=[]

    # prev_elements를 stack이라고 생각하자 DFS에서 재귀함수를 사용할 때 stack을 사용한다고 생각하자

    # 반복 조건
    # 1. 주어진 list에서 남은 숫자 넣기
    def dfs(elements):
        # list에 남은 숫자가 없으면
        if len(elements) == 0:
            # 현재 list에 쌓인 숫자들 복사해서 결과값으로 넣기
            results.append(prev_elements[:])

        for e in elements:
            # 재귀에 넣을 list 복사 -> 원본이 변경되면 안되기 때문
            next_elements = elements[:]
            # 다음에 넣을 list는 현재 값은 제외하고 넣는다.
            next_elements.remove(e)

            # stack에 값 집어넣기 DFS에서 자식 노드를 생성하는 상황
            prev_elements.append(e)
            # 재귀 함수 호출
            dfs(next_elements)
            # DFS의 경우 전체를 순회하는 것이기 때문에 이전 부모 노드로 돌아가기 위함
            prev_elements.pop()

    dfs(nums)
    return results

