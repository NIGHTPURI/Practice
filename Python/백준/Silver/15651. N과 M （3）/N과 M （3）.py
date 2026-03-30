import sys
input = sys.stdin.readline

N, M = map(int,input().split())
result = []

def solve(depth) :
    if depth == M :
        print(' '.join(map(str,result)))
        return
    
    for i in range(1, N+1) :
        result.append(i)
        
        solve(depth+1)
        
        result.pop()
        
solve(0)