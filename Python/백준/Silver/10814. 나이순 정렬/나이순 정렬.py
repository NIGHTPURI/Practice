import sys
input = sys.stdin.readline

N = int(input().strip())
age = []


for _ in range(N) :
    n, s = input().split()
    age.append((int(n),s))
    
age.sort(key=lambda x: x[0])

for n,s in age :
    print(n,s)