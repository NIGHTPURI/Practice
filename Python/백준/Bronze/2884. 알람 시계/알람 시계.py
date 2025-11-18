a, b = map(int,input().split())
if a == 0 :
    a = 24
if b < 45 :
    a -= 1
print(a%24,(b+15)%60)