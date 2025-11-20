while True:
    n = int(input())
    if n == -1:      # 종료 조건
        break

    if n == 1:       # 1은 완전수가 아님
        print("1 is NOT perfect.")
        continue

    divisors = [1]   # 1은 항상 약수

    # 2부터 √n 까지만 검사해서 약수 찾기 (효율적인 방식)
    i = 2
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:       # 서로 다른 약수 쌍이면 둘 다 추가
                divisors.append(n // i)
        i += 1

    if sum(divisors) == n:
        divisors.sort()
        print(f"{n} = " + " + ".join(map(str, divisors)))
    else:
        print(f"{n} is NOT perfect.")
