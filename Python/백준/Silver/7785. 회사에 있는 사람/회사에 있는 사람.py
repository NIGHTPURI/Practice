import sys
input = sys.stdin.readline

N = int(input())

emp = set()

for _ in range(N) :
    name, action = input().split()
    if action == 'enter' :
        emp.add(name)
    else :
        if name in emp :
            emp.remove(name)
            
emp_li = sorted(emp, reverse = True)

for e in emp_li :
    print(e)