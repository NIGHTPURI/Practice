import sys
input = sys.stdin.readline

def gcd(a,b) :
    return gcd(b,a%b) if b else a

N = int(input().strip())

tree = [int(input().strip()) for _ in range(N)]
gap = [tree[x+1] - tree[x] for x in range(N-1)]
g = gap[0]
for i in range(1,len(gap)):
    g = gcd(g,gap[i])

total_t = (tree[-1] - tree[0]) // g + 1
print(total_t - N)