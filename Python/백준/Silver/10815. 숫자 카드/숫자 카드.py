import sys
input = sys.stdin.readline


N = int(input().strip())
have = set(map(int, input().split()))


M = int(input().strip())
check = list(map(int, input().split()))


result = ['1' if x in have else '0' for x in check]
print(' '.join(result))
