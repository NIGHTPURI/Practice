r = int(input())
T = int(input())
s = 0
for t in range(1,T+1):
    a, b = map(int,input().split())
    s += a*b
if r == s :
    print("Yes")
else :
    print("No")