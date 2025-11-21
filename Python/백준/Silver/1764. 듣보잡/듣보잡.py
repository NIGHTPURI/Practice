import sys
input = sys.stdin.readline

N, M = map(int,input().split())

hear = set(input().strip() for _ in range(N))
see = set(input().strip() for _ in range(M))

both = sorted(hear & see)

print(len(both))
print('\n'.join(both))