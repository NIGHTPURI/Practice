n = int(input())

k = 1
while n > (k*(k+1))//2 :
    k += 1
    
prev = (k*(k-1))//2
idx = n-prev

if  k%2==0 :
    a = idx
    b = k-idx+1
else :
    a = k-idx+1
    b = idx
print(f"{a}/{b}")
    
    