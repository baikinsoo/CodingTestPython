import sys

def card():
    # 카드 수, 합칠 횟수 입력
    n, m = map(int, sys.stdin.readline().rstrip().split())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    # 점수를 가장 작게 만드는 방법 정렬해서 앞에 2개 더하면 끝
    sorted_arr = sorted(arr)

    # 합칠 횟수만큼 반복
    for _ in range(m):
        # 가장 작은 두 값 더하기
        total = sorted_arr[0] + sorted_arr[1]
        # 값 바꿔주기
        sorted_arr[0], sorted_arr[1] = total, total
        # 다시 정렬해주기
        sorted_arr = sorted(sorted_arr)

    return sum(sorted_arr)

if __name__ == "__main__":
    result = card()
    print(result)





