import sys
input = sys.stdin.readline

n = int(input().strip())
li = list(map(int,input().split()))

sort_li = sorted(set(li))

dic = {v : idx for idx, v in enumerate(sort_li)}

print(" ".join(str(dic[x]) for x in li))