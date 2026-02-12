N = int(input())
li = list(map(int,input().split()))
M = max(li)

print(sum(li) /M*100 /N)