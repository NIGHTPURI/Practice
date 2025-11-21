import sys
input = sys.stdin.readline

while True:
    s = input().rstrip('\n')  
    if s == '.':
        break

    stack = []
    balance = True

    for ch in s:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack[-1] != '(':
                balance = False
                break
            stack.pop()
        elif ch == ']':
            if not stack or stack[-1] != '[':
                balance = False
                break
            stack.pop()


    if stack:
        balance = False

    print('yes' if balance else 'no')
