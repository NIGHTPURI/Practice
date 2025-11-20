def fine_unique(values):
    for v in values :
        if values.count(v) == 1 :
            return v

xs = []
ys = []
for _ in range(3) :
    a, b = map(int,input().split())
    xs.append(a)
    ys.append(b)

x4 = fine_unique(xs)
y4 = fine_unique(ys)

print(x4,y4)