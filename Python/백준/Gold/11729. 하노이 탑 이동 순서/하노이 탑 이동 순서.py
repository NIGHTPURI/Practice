import sys

def hanoi(n, start, end, bypass) :
    if n == 1 :
        print(f"{start} {end}")
        return
    
    hanoi(n-1, start, bypass, end)
    
    print(f"{start} {end}")
    
    hanoi(n-1, bypass, end, start)
    

N = int(input().strip())
print(2**N-1)
hanoi(N, 1, 3, 2)
    