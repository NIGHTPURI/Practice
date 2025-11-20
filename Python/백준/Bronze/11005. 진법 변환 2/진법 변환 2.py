N, B = map(int,input().split())
s = ''
while N != 0 :
    digit = N % B
    if digit >= 10 :
        digit = chr(digit+ord('A')-10)
    else : 
        digit = chr(digit+ord('0'))
    s += digit
    N = N//B
s = s[::-1]
print(s)