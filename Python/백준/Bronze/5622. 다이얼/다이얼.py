dial = ["", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

s = input().strip()
time = 0

for ch in s:
    for i in range(1, len(dial)):       
        if ch in dial[i]:
            time += i + 2                
            break

print(time)