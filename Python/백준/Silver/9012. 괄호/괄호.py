import sys
input = sys.stdin.readline

N = int(input().strip())

for _ in range(N) :
    s = input().strip()
    stack = []
    is_vps = True
    
    for ch in s :
        if ch == '(' :
            stack.append(ch)
        else :
            if stack :
                stack.pop()
            else :
                is_vps = False
                break
    if stack :
        is_vps = False
        
    print("YES" if is_vps else "NO")