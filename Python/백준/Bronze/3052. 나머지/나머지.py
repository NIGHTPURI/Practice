s = set()
for _ in range(10) :
    a = int(input())
    a = a%42
    s.add(a)
print(len(s))