tri = list(map(int,input().split()))
tri.sort()
if tri[2] >= tri[1]+tri[0] :
    tri[2] = tri[1]+tri[0]-1
print(sum(tri))
