import sys
input = sys.stdin.readline

N, M = map(int,input().split())
board = [input().strip() for _ in range(N)]

def repaint_count(x:int, y:int) -> int:
    w = 0
    b = 0
    for i in range(8) :
        for j in range(8) :
            current = board[x+i][y+j]
            if (i+j)%2 == 0 :
                if current != 'W' :
                    w += 1
                if current != 'B' :
                    b += 1
            else :
                if current != 'B' :
                    w += 1
                if current != 'W' :
                    b += 1 
    return min(w,b)

answer = 64
for x in range(N-7):
    for y in range(M-7) :
        repaint = repaint_count(x,y)
        if repaint < answer :
            answer = repaint

print(answer)