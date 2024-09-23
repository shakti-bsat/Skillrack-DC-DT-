r,c = map(int,input().split())
q = int(input())
arr = [[0 for _ in range(c)] for _ in range(r)]
for _ in range(q):

    on,off = map(int,input().split())
    for i in range(c):
        if i != off-1:
            arr[on-1][i] = 1 - arr[on-1][i]
    
    for i in range(r):
        if i != on-1:
            arr[i][off-1] = 1 - arr[i][off-1]

    
    arr[on-1][off-1] = 1

for i in arr:
    print(*i)

