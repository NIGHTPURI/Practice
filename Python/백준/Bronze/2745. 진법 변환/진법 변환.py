n, b = input().split()
b = int(b)

v = 0
for ch in n :
    if '0' <= ch <= '9' :
        d = ord(ch) - ord('0')
    else :
        d = ord(ch) - ord('A') + 10
    v = v * b + d
print(v)
        