a, b = map(int,input().split())
li = []
n = 1
while len(li) < b :
    li.extend([n]*n)
    n += 1
print(sum(li[a-1:b]))