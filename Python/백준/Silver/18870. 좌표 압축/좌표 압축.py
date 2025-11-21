import sys

input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int,input().split()))

sorted_arr = sorted(set(arr))

coord = {v : idx for idx, v in enumerate(sorted_arr)}

print(" ".join(str(coord[x]) for x in arr))