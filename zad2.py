from cmath import sqrt


def prime(*args):
    for n in args:
        if n < 2:
            print(f"{n} is not prime")
            continue
        for i in range(2, int(sqrt(n).real) + 1):
            if n % i == 0:
                print(f"{n} is not prime")
                break
        else:
            print(f"{n} is prime number")


prime(0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, -1)
