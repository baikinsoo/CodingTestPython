n = int(input())
a = set(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

for num in targets:
    if num in a:
        print(1)
    else:
        print(0)