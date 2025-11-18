import sys
input = sys.stdin.readline

T=int(input().strip())
for t in range(1,T+1) :
    a, b = map(int,input().split())
    print(a+b)