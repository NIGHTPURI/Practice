import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int,input().split())

q = deque(range(1,N+1))
out = []

while q :
    for _ in range(K-1) :
        q.rotate(-1)
    out.append(q.popleft())

print('<' + ', '.join(map(str,out)) + '>')