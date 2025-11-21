import sys
input = sys.stdin.readline

N = input().strip()

nums = sorted(N, reverse=True)
print("".join(nums))