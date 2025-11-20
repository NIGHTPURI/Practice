N = int(input())
li = list(map(int,input().split()))

def is_prime(x: int) -> bool :
    if x < 2 :
        return False
    i=2
    while i*i <= x :
        if x%i == 0 :
            return False
        i += 1
    return True

cnt = 0
for n in li :
    if is_prime(n) :
        cnt += 1

print(cnt)
    