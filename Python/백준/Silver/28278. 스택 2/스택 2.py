import sys
input = sys.stdin.readline

T = int(input().strip())
stack = []
out = []
for t in range(1,T+1):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1 :
        stack.append(cmd[1])
    elif cmd[0] == 2 :
        if stack :
            out.append(stack.pop())
        else :
            out.append('-1')
    elif cmd[0] == 3 :
        out.append(len(stack))
    elif cmd[0] == 4 :
        if stack :
            out.append('0')
        else :
            out.append('1')
    elif cmd[0] == 5 :
        if stack :
            out.append(stack[-1])
        else :
            out.append('-1')
print(*out)
    