n, m = map(int,input().split())
li = [i for i in range(1,n+1)]

for _ in range(m) :
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    
    li[a], li[b] = li[b], li[a]
    
    
print(*li)
    