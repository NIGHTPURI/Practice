import sys
from collections import Counter
input = sys.stdin.readline

N = int(input().strip())
have = list(map(int,input().split()))
M = int(input().strip())
check = list(map(int,input().split()))

counter = Counter(have)

cnt = [str(counter[x]) for x in check]
print(' '.join(cnt))
