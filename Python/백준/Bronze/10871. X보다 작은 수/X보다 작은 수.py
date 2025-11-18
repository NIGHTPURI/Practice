import sys
input = sys.stdin.readline


n, x = map(int,input().split())
li = list(map(int,input().split()))

result = [str(num) for num in li if num < x]
print(" ".join(result))