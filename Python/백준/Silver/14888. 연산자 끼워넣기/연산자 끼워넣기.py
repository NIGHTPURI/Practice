import sys
input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int, input().split()))
p, m, s, d = map(int, input().split())

max_v = -1e9
min_v = 1e9

def solve(depth, total, p, m, s, d) :
    global min_v, max_v
    
    if depth == N :
        max_v = max(total, max_v)
        min_v = min(total, min_v)
        return
    
    
    if p > 0 :
        solve(depth + 1, total + nums[depth], p-1, m, s, d)
    if m  > 0:
        solve(depth + 1, total - nums[depth], p, m - 1, s, d)
    if s > 0:
        solve(depth + 1, total * nums[depth], p, m, s - 1, d)
    if d > 0:
        if total < 0:
            solve(depth + 1, -(-total // nums[depth]), p, m, s, d - 1)
        else:
            solve(depth + 1, total // nums[depth], p, m, s, d - 1) 
            
solve(1, nums[0], p, m, s, d)

print(max_v)
print(min_v)
        