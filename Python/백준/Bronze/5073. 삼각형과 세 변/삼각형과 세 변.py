while True :
    li = list(map(int,input().split()))
    if sum(li) == 0 :
        break
    li.sort()
    if li[2] >= li[1]+li[0] :
        print("Invalid")
    elif li[2] == li[0]:
        print("Equilateral")
    elif li[2] == li[1] or li[1] == li[0] :
        print("Isosceles")
    else :
        print("Scalene")
    