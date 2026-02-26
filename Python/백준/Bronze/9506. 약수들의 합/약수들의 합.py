while True:
    n = int(input())
    if n == -1:      
        break

    if n == 1:       
        print("1 is NOT perfect.")
        continue

    divisors = [1]   

    i = 2
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:       
                divisors.append(n // i)
        i += 1
    if sum(divisors) == n :
        divisors.sort()
        divisors_str = " + ".join(map(str,divisors))
        print(f"{n} = {divisors_str}")
    else :
        print(f"{n} is NOT perfect.")