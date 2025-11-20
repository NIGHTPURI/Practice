M = int(input())
N = int(input())
prime = [i for i in range(M,N+1)]
result = []
def is_prime(x: int):
    if x < 2 :
        return 0
    i = 2
    while i*i <= x :
        if x%i == 0 :
            return 0
        i += 1
    return x

for i in prime :
    if is_prime(i) > 0 :
        result.append(i)
if len(result) > 0 :
    print(sum(result))
    print(result[0])
else :
    print("-1")