import sys
input = sys.stdin.readline

n = int(input().strip())
li = list(map(int,input().split()))
print(min(li),max(li))