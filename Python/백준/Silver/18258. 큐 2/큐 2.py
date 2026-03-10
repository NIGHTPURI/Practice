import sys
input = sys.stdin.readline
from collections import deque

N = int(input().strip())

queue = deque()
out = []

for _ in range(N) :
    cmd = list(input().split())
    if cmd[0] == 'push' :
        queue.append(cmd[1])
    elif cmd[0] == 'pop' :
        if queue :
            out.append(queue.popleft())
        else :
            out.append('-1')
    elif cmd[0] == 'size' :
        out.append(len(queue))
    elif cmd[0] == 'empty' :
        if not queue :
            out.append('1')
        else :
            out.append('0')
    elif cmd[0] == 'front' :
        if queue :
            out.append(queue[0])
        else :
            out.append('-1')
    elif cmd[0] == 'back' :
        if queue :
            out.append(queue[-1])
        else :
            out.append('-1')
print(*out, sep='\n')
        