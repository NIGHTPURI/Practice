import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)

out = set()

for i in range(n):
    for j in range(i+1,n+1) :
        out.add(s[i:j])
        
print(len(out))