import sys
input = sys.stdin.readline

def fac(x) :
    if x <= 1 :
        return 1
    return x * fac(x-1)

N, K = map(int,input().split())

print((fac(N))//(fac(K)*fac(N-K)))
