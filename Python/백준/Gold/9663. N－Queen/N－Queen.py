import sys
input = sys.stdin.readline

N = int(input().strip())
v1 = [False] * N
v2 = [False] * (2*N-1)
v3 = [False] * (2*N-1)
ans = 0

def solve(row) :
    global ans
    if row == N :
        ans += 1
        return
    
    for col in range(N) :
        if not v1[col] and not v2[row+col] and not v3[row-col+(N-1)] :
            v1[col] = v2[row+col] = v3[row-col+(N-1)] = True
            
            solve(row+1)
            
            v1[col] = v2[row+col] = v3[row-col+(N-1)] = False
            
            
solve(0)
print(ans)