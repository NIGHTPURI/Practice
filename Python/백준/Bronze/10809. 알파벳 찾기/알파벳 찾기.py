import sys
input = sys.stdin.readline

pos = [-1]*26

s = input().strip()

for i,ch in enumerate(s) :
    idx = ord(ch) - ord("a")
    if pos[idx] == -1 :
        pos[idx] = i
        
print(*pos)
    
