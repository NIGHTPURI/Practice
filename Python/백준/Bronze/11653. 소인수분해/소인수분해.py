N = int(input())

d=2
while d*d <= N :
    while N%d == 0 :
        print(d)
        N //= d
    d += 1

if N > 1 :
    print(N)