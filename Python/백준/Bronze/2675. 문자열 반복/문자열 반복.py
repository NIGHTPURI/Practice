T = int(input())
for t in range(1,T+1) :
    n, s = input().split()
    result = ""
    for i in range(len(s)) :
        result += s[i]*int(n)
    print(result)
        