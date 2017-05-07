def is_prime(n):
        status = True
        if n < 2:
            status = False
        else:
            for i in range(2,n):
                if n % i == 0:
                    status = False
        return status

x=2
for n in range(3,102400):
    if is_prime(n):
        if x+2 == n:
            print("%d (%d = %d+2)" % (n, n, x))
        x = n
