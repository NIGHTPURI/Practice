word = input().strip().upper()

cnt = [0]*26
for ch in word:
    idx = ord(ch) - ord('A')
    cnt[idx] += 1
max_v = max(cnt)
max_i = [i for i,v in enumerate(cnt) if v == max_v]

if len(max_i) > 1 :
    print("?")
else :
    print(chr(max_i[0]+ord('A')))