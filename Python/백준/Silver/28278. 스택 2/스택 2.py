import sys
input = sys.stdin.readline

N = int(input().strip())
stack = []
out = []  

for _ in range(N):
    cmd = input().split()
    
    if cmd[0] == '1' :
        stack.append(int(cmd[1]))
    elif cmd[0] == '2' :
        if stack :
            out.append(str(stack.pop()))
        else :
            out.append('-1')
    elif cmd[0] == '3' :
        out.append(str(len(stack)))
    elif cmd[0] == '4' :
        if not stack :
            out.append('1')
        else :
            out.append('0')
    elif cmd[0] == '5' :
        if stack :
            out.append(str(stack[-1]))
        else :
            out.append('-1')
                       
print('\n'.join(out))