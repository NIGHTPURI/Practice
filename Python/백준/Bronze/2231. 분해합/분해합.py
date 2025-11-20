N = int(input())

start = max(1,N - 9*len(str(N)))
result = 0
for m in range(start,N) :
    digit_sum = sum(map(int,str(m)))
    if m + digit_sum == N :
        result = m
        break

print(result)