import sys
input = sys.stdin.readline

N = int(input().strip())
nums = [int(input().strip()) for _ in range(N)]
nums.sort()
for x in nums :
    print(x)
    