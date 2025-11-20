X = int(input())

k = 1
while X > (k*(k+1))//2 :
    k += 1

prev = (k*(k-1))//2
idx = X-prev

if k%2 == 0 :
    numerator = idx
    denominator = k-idx+1
else :
    numerator = k-idx+1
    denominator = idx

print(f"{numerator}/{denominator}")
