n = int(input())
arr = sorted(list(map(int,input().split())))[::-1]
s_dist = 0

for i in range(0,n,2):
    s_dist += 2 * arr[i] 

print(s_dist)
