import sys
input = sys.stdin.readline

T = int(input())
xl = []
yl = []

for t in range(1, T + 1):
    x, y = map(int, input().split())
    xl.append(x)
    yl.append(y)
    
if len(xl) <= 1: 
    print(0)
else:
    print((max(xl) - min(xl)) * (max(yl) - min(yl)))