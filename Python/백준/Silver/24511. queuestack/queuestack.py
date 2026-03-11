import sys
input = sys.stdin.readline
from collections import deque

N = int(input().strip())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
M = int(input().strip())
C = list(map(int,input().split()))

q_s = deque()
for i in range(N) :
    if A[i] == 0 :
        q_s.appendleft(B[i])
        
for x in C :
    q_s.append(x)
    print(q_s.popleft(), end = ' ')