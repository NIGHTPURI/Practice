import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []
ans = []
def solve(depth,start) :
    if depth == M :
        ans.append(' '.join(map(str,result))) 
        return
    
    for i in range(start, N+1) :
        result.append(i)
        
        solve(depth + 1, i)
        
        result.pop()
        
solve(0, 1)
print('\n'.join(ans))