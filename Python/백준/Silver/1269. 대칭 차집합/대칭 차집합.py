import sys
input = sys.stdin.readline

a, b = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))

amb = sorted(A-B)
bma = sorted(B-A)

print(len(amb)+len(bma))
