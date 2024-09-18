m = int(input())
n = int(input())

buses = [0] * m
for _ in range(n):
    x, y, k = map(int, input().split())
    for i in range(x-1, y):
        buses[i] +=k

print(buses)