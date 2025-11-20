N, M = map(int,input().split())
card = list(map(int,input().split()))

best = 0

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            s = card[i] + card[j] + card[k]
            if s == M :
                best = M
                print(best)
                exit()
            if s < M and s > best :
                best = s
print(best)
            