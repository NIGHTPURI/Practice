import sys
input = sys.stdin.readline

def gcd(a,b) :
    return gcd(b,a%b) if b else a

a, b = map(int, input().split())
c, d = map(int, input().split())
ja = a*d + b*c
mo = b*d
g = gcd(ja,mo)
print(ja//g, mo//g)
