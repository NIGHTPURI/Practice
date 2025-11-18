N= int(input())
li = list(map(int,input().split()))
M = max(li)
for i in range(len(li)) :
    li[i] = li[i]/M*100
print(sum(li)/N)    