board = [[0] * 100 for _ in range(100)]

n = int(input())
for _ in range(n) :
    x, y = map(int,input().split())
    for i in range(x,x+10) :
        for j in range(y,y+10) :
            board[i][j] = 1

area = 0
for i in range(100) :
    for j in range(100) :
        area += board[i][j]
print(area)
