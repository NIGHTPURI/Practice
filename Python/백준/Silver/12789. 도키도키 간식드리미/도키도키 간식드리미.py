import sys
input = sys.stdin.readline

N = int(input().strip())
stack = []
target = 1
stu = list(map(int, input().split()))
for i in stu :
    stack.append(i)
    while stack and stack[-1] == target :
        stack.pop()
        target += 1

if not stack :
    print('Nice')
else :
    print('Sad')
    
    