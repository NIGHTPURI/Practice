li = [False] * 31
for i in range(28) :
    a = int(input())
    li[a] = True
    
for i in range(1,31) :
    if not li[i] :
        print(i)