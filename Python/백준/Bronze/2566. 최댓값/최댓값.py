board = [list(map(int,input().split())) for _ in range(9)]
m = max([v for row in board for v in row])
print(m)

for i in range(9) : 
    for j in range(9) : 
        if m == board[i][j] :
            print(i+1, j+1)
            exit()