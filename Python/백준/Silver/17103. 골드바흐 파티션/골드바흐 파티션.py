import sys
input = sys.stdin.readline

max_v = 1000000
is_prime = [True] * (max_v + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(max_v**0.5)+1) :
    if is_prime :
        for j in range(i*i, max_v+1, i) :
            is_prime[j] = 0
            
T = int(input())
for t in range(1,T+1) :
    N = int(input())
    cnt = 0
    
    for k in range(2,N//2+1) :
        if is_prime[k] and is_prime[N-k] :
            cnt += 1
    
    print(cnt)
        