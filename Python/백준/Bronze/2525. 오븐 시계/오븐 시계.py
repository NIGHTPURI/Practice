h, m = map(int,input().split())
need = int(input())
m += need
if m >= 60 :
    h += (m//60)
    if h > 23 :
        h -= 24
    m %= 60
print(h,m)