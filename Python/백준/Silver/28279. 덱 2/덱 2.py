import sys
input = sys.stdin.readline
from collections import deque

d = deque()
out = []
N = int(input().strip())

for _ in range(N) :
    cmd = list(input().split())
    if cmd[0] == '1' :
        d.appendleft(cmd[1])
    elif cmd[0] == '2':
        d.append(cmd[1])
    elif cmd[0] == '3':
        if d :
            out.append(d.popleft())
        else :
            out.append('-1')
    elif cmd[0] == '4':
        if d:
            out.append(d.pop())
        else :
            out.append('-1')
    elif cmd[0] == '5':
        out.append(len(d))
    elif cmd[0] == '6':
        if not d :
            out.append('1')
        else :
            out.append('0')
    elif cmd[0] == '7':
        if d :
            out.append(d[0])
        else : 
            out.append('-1')
    elif cmd[0] == '8':
        if d :
            out.append(d[-1])
        else : 
            out.append('-1')
print('\n'.join(map(str,out)))