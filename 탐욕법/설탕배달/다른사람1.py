def algoritm2839():
    i = int(input())
    n = i
    bag5 = int(n / 5)
    n = n % 5
    while (bag5 >= 0):
        if (n % 3 == 0 or n == 0):
            bag3 = int(n / 3)
            return bag3 + bag5
        if (bag5 == 1):
            n = bag5 * 5 + n
            bag5 -= 1
        else:
            bag5 -= 1
            n = i - bag5 * 5
    return -1
print(algoritm2839())