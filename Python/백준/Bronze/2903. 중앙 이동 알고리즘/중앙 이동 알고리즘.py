i = 2
n = int(input())
v = 0
for _ in range(n) :
    i = i+(i-1)
    v = i**2
print(v)