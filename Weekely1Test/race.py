import sys
from collections import deque

def race():

    # 차량 수 입력
    k = int(input().rstrip())
    carsIn = []
    carsInDic = {}
    carsOut = []
    count = 0

    # 들어가는 차량 리스트 생성
    for _ in range(k):
        ci = input().rstrip()
        carsIn.append(ci)

    # 나오는 차량 리스트 생성
    for _ in range(k):
        co = input().rstrip()
        carsOut.append(co)

    # 들어가는 차량 순서(인덱스) 차량 이름 dic 생성
    for i, carIn in enumerate(carsIn):
        carsInDic[carIn] = i

    # 각 차량 마다 비교
    for x in range(k-1):
        for y in range(x+1,k):
            # 터널을 나온 차량 순서대로 차량의 인덱스 번호와 그 다음으로 나온 차량의 인덱스 번호를 비교
            # 먼저 나온 차량 뒤에 나온 차량보다 인덱스 무조건 작아야함
            if carsInDic[carsOut[x]] > carsInDic[carsOut[y]]:
                # 하나라도 발견하면 추월한거고 멈춘다
                count += 1
                break

    return count

if __name__ == "__main__":
    result = race()
    print(result)
