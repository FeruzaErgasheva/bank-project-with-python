def func(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum += 1
    if sum == 2:
        return True
    else:
        return False

      

n=int(input())
yangi=list(filter(func,range(1,n)))
print(yangi)


