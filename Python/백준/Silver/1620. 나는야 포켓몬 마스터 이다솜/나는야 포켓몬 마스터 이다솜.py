import sys
input = sys.stdin.readline

N, M = map(int,input().split())

idx_to_name = [None] * (N+1)
name_to_idx = {}

for i in range(1,N+1) :
    name = input().strip()
    idx_to_name[i] = name
    name_to_idx[name] = i

out = []

for _ in range(M):
    p = input().strip()
    if p.isdigit() :
        out.append(idx_to_name[int(p)])
    else :
        out.append(str(name_to_idx[p]))

for o in out :
    print(o)