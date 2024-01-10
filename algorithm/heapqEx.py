from heapq import heapify, heappop, heappush

a = [5, 3, 4, 1, 2]
heapify(a)
print(a[0])             # 1
print(heappop(a))       # 1
print(a[0])             # 2
heappush(a, 7)
print(a[0])             # 2
heappush(a, 0)
print(a[0])             # 0