M, N = map(int,input().split())

def is_prime(x) :
    if x <= 1 :
        return False
    i=2
    while i*i <= x :
        if x % i == 0 :
            return False
        i += 1
    return True

for k in range(M,N+1):
    p = is_prime(k)
    if p:
        print(k)