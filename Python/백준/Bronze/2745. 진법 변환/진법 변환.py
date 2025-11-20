N, B = input().split()
B = int(B)

value = 0
for ch in N :
    if '0' <= ch <= '9' :
        digit = ord(ch) - ord('0')
    else :
        digit = ord(ch) - ord('A') + 10
    value = value * B + digit
    
print(value)