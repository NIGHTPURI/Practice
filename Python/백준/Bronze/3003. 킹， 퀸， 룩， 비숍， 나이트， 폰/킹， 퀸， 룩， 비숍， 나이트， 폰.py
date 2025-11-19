black = [1,1,2,2,2,8]
white = list(map(int,input().split()))
result = []
for i in range(len(black)) :
    result.append(black[i]-white[i])
print(*result)