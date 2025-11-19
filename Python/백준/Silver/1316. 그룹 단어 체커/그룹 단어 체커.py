N = int(input())
count = 0
for _ in range(N) :
    s = input().strip()
    seen = set()
    prev = ''
    is_group = True
    for ch in s :
        if prev != ch :
            if ch in seen :
                is_group = False
                break
            seen.add(ch)
            prev = ch
    if is_group:
        count += 1
print(count)