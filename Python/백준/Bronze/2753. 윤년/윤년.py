a = int(input())
r = 0
if (a%4)==0 and ((a%100!=0) or (a%400==0)) :
    r += 1
print(r)    