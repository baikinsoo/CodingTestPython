import sys

def balance():

    # 문제에서 두개의 기호가 주어졌다.
    pair = {
        ')' : '(',
        ']' : '[',
    }

    # stack과 결과를 넣을 list 생성
    stack = []
    results = []

    while True:
        _str = sys.stdin.readline().rstrip()
        is_balanced = True
        if not _str or _str == '.':
            break

        for x in _str:
            if x in pair.values():
                stack.append(x)
            elif x in pair.keys():
                if not stack:
                    is_balanced = False
                    break
                char = stack.pop()
                if pair[x] != char:
                    is_balanced = False
                    break

        if stack:
            is_balanced = False
        if is_balanced:
            print('yes')
        elif not stack:
            print('no')
        else:
            print('no')

    return results

if __name__ == "__main__":
    result = balance()
    for res in result:
        print(res)
