board = [input().strip() for _ in range(5)]
s = ''
for i in range(15):
    for j in range(5):
        if i < len(board[j]) :
            s = s + board[j][i]
print(s)