T = int(input())
for t in range(1,T+1) :
    n = int(input())
    exc = [0]*4
    if n >= 25 :
        exc[0] = n//25
        n %= 25
    if n >= 10 :
        exc[1] = n//10
        n %= 10
    if n >= 5 :
        exc[2] = n//5
        n %= 5
    if n >= 1 :
        exc[3] = n//1
    print(*exc)

    
