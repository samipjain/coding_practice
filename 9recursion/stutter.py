import math

def stutter(n):
    if n < 10:
        return (10 * n) + n
    else:
        a = stutter(math.floor(n/10))
        b = stutter(math.floor(n%10))
        return (100 * a) + b

if __name__ == "__main__":
    print(stutter(3489))