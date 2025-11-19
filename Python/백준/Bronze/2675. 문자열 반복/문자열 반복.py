T = int(input())
for t in range(1,T+1) :
    r, s = input().split()
    p = ""
    for ch in s:
        p += ch*int(r)
    print(p)

