n = int(input())
li = list(map(int,input().split()))
cnt = 0
for k in li :
    if k == 1 :
        continue
    is_true = True
    i = 2
    while i*i <= k :
        if k%i == 0 :
            is_true = False
            break
        i += 1
    if is_true :
        cnt += 1
print(cnt)
        
        