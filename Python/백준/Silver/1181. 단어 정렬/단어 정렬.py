import sys
input = sys.stdin.readline

N = int(input().strip())
words = set()

for _ in range(N):
    words.add(input().strip())

words_list = list(words)

words_list.sort(key=lambda w: (len(w), w))

for w in words_list:
    print(w)
