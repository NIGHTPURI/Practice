import sys
input = sys.stdin.readline

def is_prime(x) :
    if x <= 1: return False
    
    i = 2
    while i*i <= x :
        if x%i == 0 :
            return False
        i += 1
    return True

n = int(input().strip())

for _ in range(n) :
    a = int(input().strip())
    while True:
        if is_prime(a):
            print(a)
            break
        a += 1
    